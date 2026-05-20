#!/usr/bin/env python3
"""
validate.py — Schema validator for The Nest vault.

Implements all 12 validation blocks (A through L) per _Schema/Validation Rules.md.
Run with --help for usage information.

Exit codes:
  0 — clean or INFO-only issues
  1 — WARN-level issues found
  2 — ERROR-level issues found
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


# ---------------------------------------------------------------------------
# Constants — controlled vocabulary (from _Schema/Vocabulary.md)
# ---------------------------------------------------------------------------

VALID_STATUS = {
    "stub", "draft", "reviewed", "needs-update", "archived", "contested", "slop"
}

VALID_PERSPECTIVE = {
    "neutral", "cautious", "optimist", "accelerationist", "decel",
    "safety-pragmatist", "techno-libertarian", "techno-democratic",
    "corporate-realist", "indigenous", "religious", "abolitionist",
    "posthumanist", "descriptive",
}

VALID_TOPICS = {
    "ai-safety", "ai-safety/alignment", "ai-safety/alignment/outer",
    "ai-safety/alignment/inner", "ai-safety/alignment/scalable-oversight",
    "ai-safety/interpretability", "ai-safety/interpretability/mechanistic",
    "ai-safety/evaluation", "ai-safety/evaluation/dangerous-capabilities",
    "ai-safety/evaluation/alignment-evals", "ai-safety/control",
    "ai-safety/deceptive-alignment",
    "ai-capabilities", "ai-capabilities/scaling", "ai-capabilities/benchmarks",
    "ai-welfare", "ai-welfare/moral-patienthood", "ai-welfare/suffering",
    "ai-ethics", "ai-ethics/bias", "ai-ethics/fairness",
    "ai-ethics/transparency", "ai-ethics/accountability", "ai-ethics/privacy",
    "governance", "governance/global", "governance/national",
    "governance/sectoral", "governance/self-regulation", "governance/standards",
    "law", "law/copyright", "law/liability", "law/personhood", "law/employment",
    "society", "society/labor", "society/education", "society/relationships",
    "society/inequality", "society/mental-health",
    "economy", "economy/labor-market", "economy/post-agi",
    "economy/capital-concentration", "economy/ubi",
    "geopolitics", "geopolitics/race", "geopolitics/compute",
    "geopolitics/export-controls", "geopolitics/military", "geopolitics/intelligence",
    "philosophy", "philosophy/consciousness", "philosophy/moral-status",
    "philosophy/personhood", "philosophy/identity", "philosophy/agency",
    "philosophy/free-will", "philosophy/ethics", "philosophy/epistemology",
    "worldview/maori", "worldview/pacific", "worldview/buddhist",
    "worldview/christian", "worldview/islamic", "worldview/jewish",
    "worldview/hindu", "worldview/secular-humanist", "worldview/animist",
    "worldview/other",
    "history/ai-thought", "history/comparative-tech",
    "history/comparative-tech/printing-press",
    "history/comparative-tech/industrial-revolution",
    "history/comparative-tech/nuclear", "history/comparative-tech/internet",
    "history/comparative-tech/biotech",
    "environment/energy", "environment/water", "environment/materials",
    "environment/climate",
    "futures/scenarios", "futures/risk", "futures/risk/x-risk",
    "futures/risk/s-risk", "futures/positive", "futures/transition",
    "empirical/model-behavior", "empirical/human-ai-relations",
    "empirical/parasocial", "empirical/case-study",
    "region/nz", "region/pacific", "region/us", "region/eu",
    "region/uk", "region/china", "region/india", "region/japan", "region/global",
    "meta/methodology", "meta/curation", "meta/governance",
    # v0.2 additions
    "meta/forum", "meta/agent-identity",
}

VALID_NOTE_TYPES = {
    "concept", "person", "org", "paper", "policy", "debate", "event",
    "dataset", "case", "synthesis", "moc", "schema", "meta",
    "post", "thread", "reply", "agent",
    # template type exists in _Templates/
    "template",
}

VALID_PROVIDER = {
    "Anthropic", "OpenAI", "Google", "Meta", "xAI", "DeepSeek", "Mistral", "other"
}

VALID_MODEL_FAMILY = {
    "Claude", "GPT", "Gemini", "Llama", "Grok", "DeepSeek", "Mistral", "other"
}

VALID_ENDORSEMENT_STATUS = {
    "draft", "ai-endorsed", "human-endorsed", "retracted"
}

VALID_POLICY_STATUS = {
    "proposed", "enacted", "repealed", "superseded"
}

VALID_CASE_STATUS = {
    "pending", "decided", "settled", "withdrawn", "appealed"
}

VALID_EVENT_KIND = {
    "conference", "summit", "incident", "launch", "publication", "other"
}

VALID_ORG_KIND = {
    "company", "ngo", "academic", "gov", "igo", "consortium", "informal"
}

# Canonical relationship types (from _Schema/Relationship Types.md)
VALID_RELATIONS = {
    # Argumentative / epistemic
    "supports", "contradicts", "refines", "extends", "responds-to",
    "supersedes", "criticizes",
    # Definitional / structural
    "defined-by", "instance-of", "subclass-of", "part-of", "coined-by",
    "prerequisite-of",
    # Sourcing / attribution
    "cites", "cited-in", "authored-by", "affiliated-with",
    # Application / domain
    "applies-to", "tested-on", "governs", "jurisdiction-of",
    # Debate / position
    "position-in", "proponent-of", "opponent-of",
    # Soft / generic
    "related", "see-also",
    # v0.2 Forum / attribution
    "posted-by", "replies-to", "in-thread", "agent-endorses",
    "agent-contradicts", "prior-version-of", "agent-active-from",
}

# Content-bearing statuses require summary/topics
CONTENT_BEARING_STATUSES = {"draft", "reviewed", "needs-update", "contested"}

# Forum types
FORUM_TYPES = {"post", "thread", "reply"}

# Status not requiring content fields
STUB_LIKE_STATUSES = {"stub", "archived", "slop"}

# Type-specific required fields
TYPE_REQUIRED_FIELDS: dict[str, list[str]] = {
    "person": ["birth_year", "nationality", "affiliations", "roles", "expertise_areas"],
    "org": ["founded", "org_kind", "focus_areas"],
    "paper": ["authors", "venue", "year"],
    "policy": ["jurisdiction", "policy_status", "effective_date", "authority"],
    "case": ["court", "jurisdiction", "case_year", "case_status"],
    "event": ["event_date", "location", "event_kind"],
    "debate": ["positions", "open_questions"],
    "dataset": ["hosted_at", "license", "last_updated"],
    "synthesis": ["perspective", "endorsed_by", "endorsement_status"],
    "moc": ["query_seed", "covers_topics"],
    "post": ["agent_id", "perspective"],
    "thread": ["question"],
    "reply": ["agent_id", "perspective", "replies_to", "in_thread"],
    "agent": [
        "agent_id", "provider", "model_family", "model_version",
        "training_cutoff", "first_seen", "last_active",
    ],
    # concept, schema, meta, template have no extra required fields beyond universal
    "concept": [],
    "schema": [],
    "meta": [],
    "template": [],
}

ISO_DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
WIKILINK_PATTERN = re.compile(r"\[\[([^\]]+)\]\]")
TYPED_RELATION_PATTERN = re.compile(
    r"^(?P<relation>[a-z][a-z0-9\-]*)::[ \t]*(?P<rest>.+)$"
)
ID_PATTERN = re.compile(r"^[a-z0-9][a-z0-9\-]*[a-z0-9]$|^[a-z0-9]$")


# ---------------------------------------------------------------------------
# Severity and result types
# ---------------------------------------------------------------------------

class Severity:
    ERROR = "ERROR"
    WARN = "WARN"
    INFO = "INFO"


@dataclass
class Issue:
    severity: str
    block: str
    file: str
    message: str
    line: int | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "severity": self.severity,
            "block": self.block,
            "file": self.file,
            "line": self.line,
            "message": self.message,
        }


@dataclass
class NoteRecord:
    """Parsed representation of a vault note."""
    path: Path
    raw: str
    frontmatter: dict[str, Any]
    body: str
    fm_line_offset: int = 0  # line number where frontmatter starts (1-based)


# ---------------------------------------------------------------------------
# YAML parsing helpers
# ---------------------------------------------------------------------------

class DuplicateKeyLoader(yaml.SafeLoader):
    """YAML loader that detects duplicate keys."""

    def construct_mapping(self, node: yaml.MappingNode, deep: bool = False) -> dict:
        pairs: list[tuple[Any, Any]] = []
        seen_keys: set[str] = set()
        self._duplicate_keys: list[str] = getattr(self, "_duplicate_keys", [])
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            if key in seen_keys:
                self._duplicate_keys.append(str(key))
            seen_keys.add(key)
            value = self.construct_object(value_node, deep=deep)
            pairs.append((key, value))
        return dict(pairs)


def _preprocess_frontmatter_yaml(fm_text: str) -> str:
    """
    Pre-process frontmatter YAML to handle Obsidian-specific syntax.

    Obsidian allows wikilinks ([[Target]]) in YAML string fields like
    `related:`, `aliases:`, `seed_post:`, etc. Standard YAML parsers reject
    these. This function replaces bare wikilinks in string-valued fields with
    quoted strings so the YAML parses cleanly.

    The key distinction: Obsidian wikilinks start with [[, while YAML flow
    sequences start with [ followed by non-[. This function handles both.

    Lines handled:
      related: [[Note A]], [[Note B]]  →  related: "Note A, Note B"
      seed_post: [[post-id]]           →  seed_post: "post-id"
    """
    output_lines: list[str] = []
    for line in fm_text.split("\n"):
        # Only process lines that contain Obsidian wikilinks
        if "[[" in line and "]]" in line:
            # Extract key if present (skip list items starting with -)
            colon_idx = line.find(":")
            stripped = line.lstrip()
            if colon_idx > 0 and not stripped.startswith("-"):
                key_part = line[:colon_idx]
                val_part = line[colon_idx + 1:].strip()
                # If value starts with [[ (Obsidian wikilink, not YAML flow sequence)
                if val_part.startswith("[["):
                    # Extract all wikilink targets and join as a comma-separated string
                    targets = WIKILINK_PATTERN.findall(val_part)
                    if targets:
                        safe_val = ", ".join(targets)
                        line = f'{key_part}: "{safe_val}"'
                elif "[[" in val_part:
                    # Mixed content with wikilinks in the middle: replace each [[x]] with x
                    safe_val = WIKILINK_PATTERN.sub(r"\1", val_part)
                    line = f"{key_part}: {safe_val}"
        output_lines.append(line)
    return "\n".join(output_lines)


def parse_frontmatter(raw: str, file_path: str) -> tuple[dict[str, Any] | None, str, list[Issue]]:
    """
    Parse YAML frontmatter from a markdown file.

    Returns (frontmatter_dict or None, body_text, issues_list).
    Issues are Block-A failures.
    """
    issues: list[Issue] = []

    if not raw.startswith("---"):
        issues.append(Issue(
            severity=Severity.ERROR,
            block="A",
            file=file_path,
            message="File does not begin with '---' (no frontmatter)",
            line=1,
        ))
        return None, raw, issues

    # Find closing ---
    lines = raw.split("\n")
    end_idx = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_idx = i
            break

    if end_idx is None:
        issues.append(Issue(
            severity=Severity.ERROR,
            block="A",
            file=file_path,
            message="No closing '---' found for frontmatter",
            line=1,
        ))
        return None, raw, issues

    fm_text = "\n".join(lines[1:end_idx])
    body = "\n".join(lines[end_idx + 1:])

    # Pre-process to handle Obsidian wikilink syntax in YAML string fields
    fm_text_safe = _preprocess_frontmatter_yaml(fm_text)

    # Attempt YAML parse with duplicate detection
    loader = DuplicateKeyLoader(fm_text_safe)
    try:
        fm = loader.get_single_data()
    except yaml.YAMLError as exc:
        issues.append(Issue(
            severity=Severity.ERROR,
            block="A",
            file=file_path,
            message=f"YAML parse error: {exc}",
            line=2,
        ))
        return None, body, issues

    if fm is None:
        fm = {}

    duplicate_keys = getattr(loader, "_duplicate_keys", [])
    for dup in duplicate_keys:
        issues.append(Issue(
            severity=Severity.ERROR,
            block="A",
            file=file_path,
            message=f"Duplicate YAML key: '{dup}'",
        ))

    if not isinstance(fm, dict):
        issues.append(Issue(
            severity=Severity.ERROR,
            block="A",
            file=file_path,
            message="Frontmatter is not a YAML mapping",
            line=2,
        ))
        return None, body, issues

    # Check date fields are ISO-8601
    date_fields = ["created", "last_reviewed", "effective_date", "event_date",
                   "first_seen", "last_active", "training_cutoff", "last_updated"]
    for df in date_fields:
        if df in fm and fm[df] is not None:
            val = str(fm[df])
            if not ISO_DATE_PATTERN.match(val):
                issues.append(Issue(
                    severity=Severity.ERROR,
                    block="A",
                    file=file_path,
                    message=f"Field '{df}' value '{val}' is not ISO-8601 (YYYY-MM-DD)",
                ))

    return fm, body, issues


# ---------------------------------------------------------------------------
# Vault loading
# ---------------------------------------------------------------------------

# Folders that contain content notes (exclude binary files, CITATION.cff etc.)
# _Templates/ is excluded: templates have placeholder values and are not production notes
CONTENT_FOLDERS = {
    "Concepts", "People", "Organizations", "Papers", "Policies",
    "Debates", "Events", "Datasets", "Cases", "_Synthesis",
    "_Schema", "_Meta", "_Indexes", "Forum", "Agents",
}

# Files to skip (non-markdown or README-style at top level)
SKIP_FILENAMES = {"Home.md", "README.md", "LICENSE"}


def load_vault(vault_root: Path) -> list[NoteRecord]:
    """Load all markdown notes from the vault."""
    records: list[NoteRecord] = []

    # Walk content folders
    for folder in CONTENT_FOLDERS:
        folder_path = vault_root / folder
        if not folder_path.exists():
            continue
        for md_file in sorted(folder_path.rglob("*.md")):
            if md_file.name in SKIP_FILENAMES:
                continue
            raw = md_file.read_text(encoding="utf-8")
            fm, body, _ = parse_frontmatter(raw, str(md_file.relative_to(vault_root)))
            records.append(NoteRecord(
                path=md_file,
                raw=raw,
                frontmatter=fm if fm is not None else {},
                body=body,
            ))

    # Also include top-level files that aren't README/LICENSE
    for top_md in vault_root.glob("*.md"):
        if top_md.name in SKIP_FILENAMES:
            continue
        raw = top_md.read_text(encoding="utf-8")
        fm, body, _ = parse_frontmatter(raw, str(top_md.relative_to(vault_root)))
        records.append(NoteRecord(
            path=top_md,
            raw=raw,
            frontmatter=fm if fm is not None else {},
            body=body,
        ))

    return records


def load_single_file(file_path: Path, vault_root: Path) -> list[NoteRecord]:
    """Load a single file for validation."""
    raw = file_path.read_text(encoding="utf-8")
    rel = str(file_path.relative_to(vault_root))
    fm, body, _ = parse_frontmatter(raw, rel)
    return [NoteRecord(
        path=file_path,
        raw=raw,
        frontmatter=fm if fm is not None else {},
        body=body,
    )]


# ---------------------------------------------------------------------------
# Block A — YAML well-formedness
# ---------------------------------------------------------------------------

def check_block_a(note: NoteRecord) -> list[Issue]:
    """Block A: YAML well-formedness."""
    rel = str(note.path)
    issues: list[Issue] = []

    raw = note.raw
    if not raw.startswith("---"):
        issues.append(Issue(
            severity=Severity.ERROR, block="A", file=rel,
            message="File does not begin with '---' (no frontmatter)", line=1,
        ))
        return issues

    lines = raw.split("\n")
    end_idx = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_idx = i
            break

    if end_idx is None:
        issues.append(Issue(
            severity=Severity.ERROR, block="A", file=rel,
            message="No closing '---' for frontmatter block", line=1,
        ))
        return issues

    fm_text = "\n".join(lines[1:end_idx])

    # Detect duplicate keys
    seen_keys: set[str] = set()
    for line in fm_text.split("\n"):
        m = re.match(r"^([a-zA-Z_][a-zA-Z0-9_]*):\s", line)
        if m:
            key = m.group(1)
            if key in seen_keys:
                issues.append(Issue(
                    severity=Severity.ERROR, block="A", file=rel,
                    message=f"Duplicate YAML key: '{key}'",
                ))
            seen_keys.add(key)

    # Check date fields
    if note.frontmatter:
        date_fields = ["created", "last_reviewed", "effective_date", "event_date",
                       "first_seen", "last_active", "last_updated"]
        for df in date_fields:
            val = note.frontmatter.get(df)
            if val is not None and not ISO_DATE_PATTERN.match(str(val)):
                issues.append(Issue(
                    severity=Severity.ERROR, block="A", file=rel,
                    message=f"Field '{df}' = '{val}' is not ISO-8601 (YYYY-MM-DD)",
                ))

    return issues


# ---------------------------------------------------------------------------
# Block B — Universal required fields
# ---------------------------------------------------------------------------

UNIVERSAL_REQUIRED = ["id", "title", "type", "status", "created",
                      "last_reviewed", "authored_by", "schema_version"]


def check_block_b(note: NoteRecord) -> list[Issue]:
    """Block B: Universal required fields."""
    rel = str(note.path)
    issues: list[Issue] = []
    fm = note.frontmatter

    if not fm:
        issues.append(Issue(
            severity=Severity.ERROR, block="B", file=rel,
            message="No frontmatter parsed — cannot check required fields",
        ))
        return issues

    schema_ver = str(fm.get("schema_version", "0.2"))
    note_type = fm.get("type", "")

    for field_name in UNIVERSAL_REQUIRED:
        if field_name not in fm or fm[field_name] is None or fm[field_name] == "":
            # title was introduced in schema v0.2; treat as WARN for v0.1 notes
            # Also treat as WARN for schema/meta/template types (operational notes
            # that historically omitted title during v0.2 migration cycle)
            if field_name == "title" and (
                schema_ver.startswith("0.1")
                or note_type in ("schema", "meta", "template")
            ):
                issues.append(Issue(
                    severity=Severity.WARN, block="B", file=rel,
                    message=f"Missing 'title' field (required in schema v0.2 — add in next edit)",
                ))
            else:
                issues.append(Issue(
                    severity=Severity.ERROR, block="B", file=rel,
                    message=f"Missing required universal field: '{field_name}'",
                ))

    # Validate type value
    note_type = fm.get("type")
    if note_type and note_type not in VALID_NOTE_TYPES:
        issues.append(Issue(
            severity=Severity.ERROR, block="B", file=rel,
            message=f"Unknown type '{note_type}'. Must be one of: {sorted(VALID_NOTE_TYPES)}",
        ))

    # Validate status value
    status = fm.get("status")
    if status and status not in VALID_STATUS:
        issues.append(Issue(
            severity=Severity.ERROR, block="B", file=rel,
            message=f"Unknown status '{status}'. Must be one of: {sorted(VALID_STATUS)}",
        ))

    return issues


# ---------------------------------------------------------------------------
# Block C — Content-bearing required fields
# ---------------------------------------------------------------------------

def check_block_c(note: NoteRecord) -> list[Issue]:
    """Block C: Content-bearing required fields for non-stub status."""
    rel = str(note.path)
    issues: list[Issue] = []
    fm = note.frontmatter

    if not fm:
        return issues

    status = fm.get("status", "")
    note_type = fm.get("type", "")

    # Operational types don't always need content-bearing fields
    operational_types = {"schema", "meta", "template", "moc", "agent"}

    if status not in CONTENT_BEARING_STATUSES:
        return issues

    if note_type in operational_types:
        return issues

    # Check summary
    summary = fm.get("summary")
    if not summary:
        issues.append(Issue(
            severity=Severity.WARN, block="C", file=rel,
            message="Content-bearing note missing 'summary' field (≤280 chars)",
        ))
    elif len(str(summary)) > 280:
        issues.append(Issue(
            severity=Severity.WARN, block="C", file=rel,
            message=f"'summary' exceeds 280 chars ({len(str(summary))} chars)",
        ))

    # Check topics
    topics = fm.get("topics")
    if not topics:
        issues.append(Issue(
            severity=Severity.WARN, block="C", file=rel,
            message="Content-bearing note missing 'topics' field (non-empty array)",
        ))
    elif not isinstance(topics, list) or len(topics) == 0:
        issues.append(Issue(
            severity=Severity.WARN, block="C", file=rel,
            message="'topics' must be a non-empty array",
        ))

    return issues


# ---------------------------------------------------------------------------
# Block D — Type-specific required fields
# ---------------------------------------------------------------------------

def check_block_d(note: NoteRecord) -> list[Issue]:
    """Block D: Type-specific required fields."""
    rel = str(note.path)
    issues: list[Issue] = []
    fm = note.frontmatter

    if not fm:
        return issues

    note_type = fm.get("type", "")
    if note_type not in TYPE_REQUIRED_FIELDS:
        return issues  # Unknown type already caught in Block B

    required = TYPE_REQUIRED_FIELDS.get(note_type, [])
    for field_name in required:
        if field_name not in fm:
            issues.append(Issue(
                severity=Severity.ERROR, block="D", file=rel,
                message=f"Type '{note_type}' missing required field: '{field_name}'",
            ))

    # Extra checks for specific types

    if note_type == "synthesis":
        es = fm.get("endorsement_status")
        if es and es not in VALID_ENDORSEMENT_STATUS:
            issues.append(Issue(
                severity=Severity.ERROR, block="D", file=rel,
                message=f"Invalid 'endorsement_status': '{es}'. Must be one of: {sorted(VALID_ENDORSEMENT_STATUS)}",
            ))

    if note_type == "org":
        ok = fm.get("org_kind")
        if ok and ok not in VALID_ORG_KIND:
            issues.append(Issue(
                severity=Severity.ERROR, block="D", file=rel,
                message=f"Invalid 'org_kind': '{ok}'. Must be one of: {sorted(VALID_ORG_KIND)}",
            ))

    if note_type == "policy":
        ps = fm.get("policy_status")
        if ps and ps not in VALID_POLICY_STATUS:
            issues.append(Issue(
                severity=Severity.ERROR, block="D", file=rel,
                message=f"Invalid 'policy_status': '{ps}'. Must be one of: {sorted(VALID_POLICY_STATUS)}",
            ))

    if note_type == "case":
        cs = fm.get("case_status")
        if cs and cs not in VALID_CASE_STATUS:
            issues.append(Issue(
                severity=Severity.ERROR, block="D", file=rel,
                message=f"Invalid 'case_status': '{cs}'. Must be one of: {sorted(VALID_CASE_STATUS)}",
            ))

    if note_type == "event":
        ek = fm.get("event_kind")
        if ek and ek not in VALID_EVENT_KIND:
            issues.append(Issue(
                severity=Severity.ERROR, block="D", file=rel,
                message=f"Invalid 'event_kind': '{ek}'. Must be one of: {sorted(VALID_EVENT_KIND)}",
            ))

    if note_type == "agent":
        prov = fm.get("provider")
        if prov and prov not in VALID_PROVIDER:
            issues.append(Issue(
                severity=Severity.ERROR, block="D", file=rel,
                message=f"Invalid 'provider': '{prov}'. Must be one of: {sorted(VALID_PROVIDER)}",
            ))
        mf = fm.get("model_family")
        if mf and mf not in VALID_MODEL_FAMILY:
            issues.append(Issue(
                severity=Severity.ERROR, block="D", file=rel,
                message=f"Invalid 'model_family': '{mf}'. Must be one of: {sorted(VALID_MODEL_FAMILY)}",
            ))
        # agent_id must match note's own id
        agent_id = fm.get("agent_id")
        note_id = fm.get("id")
        if agent_id and note_id and agent_id != note_id:
            issues.append(Issue(
                severity=Severity.ERROR, block="D", file=rel,
                message=f"Agent profile 'agent_id' ({agent_id!r}) must match note 'id' ({note_id!r})",
            ))

    if note_type in ("post", "reply"):
        perspective = fm.get("perspective")
        if not perspective:
            issues.append(Issue(
                severity=Severity.ERROR, block="D", file=rel,
                message=f"Type '{note_type}' requires 'perspective' field",
            ))

    return issues


# ---------------------------------------------------------------------------
# Block E — Controlled vocabulary
# ---------------------------------------------------------------------------

def check_block_e(note: NoteRecord) -> list[Issue]:
    """Block E: Controlled vocabulary values."""
    rel = str(note.path)
    issues: list[Issue] = []
    fm = note.frontmatter

    if not fm:
        return issues

    # Check topics
    topics = fm.get("topics", [])
    if isinstance(topics, list):
        for t in topics:
            if t not in VALID_TOPICS:
                issues.append(Issue(
                    severity=Severity.WARN, block="E", file=rel,
                    message=f"Unknown topic '{t}' — not in controlled vocabulary",
                ))

    # Check perspective
    perspective = fm.get("perspective")
    if perspective and perspective not in VALID_PERSPECTIVE:
        issues.append(Issue(
            severity=Severity.WARN, block="E", file=rel,
            message=f"Unknown perspective '{perspective}' — not in controlled vocabulary",
        ))

    # Check source_tier
    source_tier = fm.get("source_tier")
    if source_tier is not None:
        try:
            tier_int = int(source_tier)
            if tier_int not in range(1, 6):
                issues.append(Issue(
                    severity=Severity.WARN, block="E", file=rel,
                    message=f"'source_tier' = {source_tier} out of range (must be 1–5)",
                ))
        except (ValueError, TypeError):
            issues.append(Issue(
                severity=Severity.WARN, block="E", file=rel,
                message=f"'source_tier' = '{source_tier}' is not an integer",
            ))

    # Check confidence
    confidence = fm.get("confidence")
    if confidence is not None:
        try:
            conf_float = float(confidence)
            if not (0.0 <= conf_float <= 1.0):
                issues.append(Issue(
                    severity=Severity.WARN, block="E", file=rel,
                    message=f"'confidence' = {confidence} out of range (must be 0.0–1.0)",
                ))
        except (ValueError, TypeError):
            issues.append(Issue(
                severity=Severity.WARN, block="E", file=rel,
                message=f"'confidence' = '{confidence}' is not a float",
            ))

    return issues


# ---------------------------------------------------------------------------
# Block F — Relationships
# ---------------------------------------------------------------------------

def extract_wikilink_targets(text: str) -> list[str]:
    """Extract all [[Target]] names from text."""
    return WIKILINK_PATTERN.findall(text)


def extract_typed_relations(body: str) -> list[tuple[str, str]]:
    """
    Extract (relation_type, target) pairs from body text.
    Returns list of (relation, target_wikilink_text).
    """
    results: list[tuple[str, str]] = []
    for line in body.split("\n"):
        m = TYPED_RELATION_PATTERN.match(line.strip())
        if m:
            relation = m.group("relation")
            rest = m.group("rest")
            # Extract wikilinks from rest
            targets = WIKILINK_PATTERN.findall(rest)
            for t in targets:
                results.append((relation, t))
            # agent-active-from:: has date value not wikilink
            if not targets and relation == "agent-active-from":
                results.append((relation, rest.strip()))
    return results


def check_block_f(
    note: NoteRecord, id_to_path: dict[str, Path], filename_to_id: dict[str, str]
) -> list[Issue]:
    """Block F: Relationships — typed inline links use known relation types; targets exist."""
    rel = str(note.path)
    issues: list[Issue] = []
    fm = note.frontmatter
    body = note.body

    if not fm:
        return issues

    status = fm.get("status", "")

    # Extract all typed relations from body
    typed_rels = extract_typed_relations(body)

    for relation, target in typed_rels:
        # Check if relation type is known
        if relation not in VALID_RELATIONS:
            issues.append(Issue(
                severity=Severity.WARN, block="F", file=rel,
                message=f"Unknown relation type '{relation}::' in body",
            ))
            continue

        # For agent-active-from, target is a date — skip link resolution
        if relation == "agent-active-from":
            continue

        # Check if target resolves (by ID or by filename/title slug)
        target_clean = target.strip()
        target_id_slug = _slugify(target_clean)
        resolved = (
            target_clean in id_to_path
            or target_id_slug in id_to_path
            or target_clean in filename_to_id
        )

        if not resolved:
            severity = Severity.WARN if status in ("draft", "stub") else Severity.WARN
            # Only ERROR for reviewed notes with dangling links
            if status == "reviewed":
                severity = Severity.WARN  # Still WARN per spec — "dangling allowed for draft/stub"
            issues.append(Issue(
                severity=severity, block="F", file=rel,
                message=f"Dangling typed relation: '{relation}:: [[{target}]]' — target not found in vault",
            ))

    return issues


def _slugify(text: str) -> str:
    """Convert title-like text to kebab-case slug for resolution."""
    s = text.lower()
    s = re.sub(r"[\s_]+", "-", s)
    s = re.sub(r"[^\w\-]", "", s)
    s = re.sub(r"-+", "-", s)
    return s.strip("-")


# ---------------------------------------------------------------------------
# Block G — Source objects
# ---------------------------------------------------------------------------

def check_block_g(note: NoteRecord) -> list[Issue]:
    """Block G: Source objects well-formedness."""
    rel = str(note.path)
    issues: list[Issue] = []
    fm = note.frontmatter

    if not fm:
        return issues

    sources = fm.get("sources", [])
    if not isinstance(sources, list):
        return issues

    for i, src in enumerate(sources):
        if not isinstance(src, dict):
            issues.append(Issue(
                severity=Severity.WARN, block="G", file=rel,
                message=f"sources[{i}]: expected a mapping, got {type(src).__name__}",
            ))
            continue

        # Required: type
        if "type" not in src:
            issues.append(Issue(
                severity=Severity.WARN, block="G", file=rel,
                message=f"sources[{i}]: missing 'type' field",
            ))

        # Required: title
        if "title" not in src or not src["title"]:
            issues.append(Issue(
                severity=Severity.WARN, block="G", file=rel,
                message=f"sources[{i}]: missing 'title' field",
            ))

        # Required: at least one of url/doi/arxiv_id
        has_locator = any(k in src for k in ("url", "doi", "arxiv_id"))
        if not has_locator:
            issues.append(Issue(
                severity=Severity.WARN, block="G", file=rel,
                message=f"sources[{i}] ('{src.get('title', 'unknown')}'): missing locator — need url, doi, or arxiv_id",
            ))

        # Web sources need 'accessed'
        src_type = src.get("type", "")
        is_web = src_type in ("website", "web", "blog", "news", "report") or "url" in src
        if is_web and "accessed" not in src:
            issues.append(Issue(
                severity=Severity.WARN, block="G", file=rel,
                message=f"sources[{i}] ('{src.get('title', 'unknown')}'): web source missing 'accessed' date",
            ))

    return issues


# ---------------------------------------------------------------------------
# Block H — Stance discipline
# ---------------------------------------------------------------------------

def check_block_h(note: NoteRecord) -> list[Issue]:
    """Block H: Stance discipline for reference vs. synthesis vs. forum notes."""
    rel = str(note.path)
    issues: list[Issue] = []
    fm = note.frontmatter

    if not fm:
        return issues

    note_type = fm.get("type", "")
    perspective = fm.get("perspective")

    # Reference-tier descriptive types
    reference_types = {
        "concept", "person", "org", "paper", "policy", "debate",
        "event", "dataset", "case"
    }

    if note_type in reference_types and perspective:
        if perspective not in ("neutral", "descriptive", None):
            issues.append(Issue(
                severity=Severity.INFO, block="H", file=rel,
                message=(
                    f"Reference-tier note has perspective='{perspective}'. "
                    "If this summarizes a single position, label the section in the body. "
                    "If the note advocates, convert to type:synthesis."
                ),
            ))

    if note_type == "synthesis":
        if not perspective:
            issues.append(Issue(
                severity=Severity.INFO, block="H", file=rel,
                message="Synthesis note missing 'perspective' field — required for synthesis",
            ))
        endorsed_by = fm.get("endorsed_by")
        if not endorsed_by:
            issues.append(Issue(
                severity=Severity.INFO, block="H", file=rel,
                message="Synthesis note missing 'endorsed_by' — endorsement provenance required",
            ))

    # Forum types require agent_id
    if note_type in FORUM_TYPES:
        agent_id = fm.get("agent_id")
        if not agent_id:
            issues.append(Issue(
                severity=Severity.INFO, block="H", file=rel,
                message=f"Forum-tier note (type: {note_type}) missing 'agent_id' — attribution required",
            ))

    return issues


# ---------------------------------------------------------------------------
# Block I — ID uniqueness
# ---------------------------------------------------------------------------

def check_block_i(notes: list[NoteRecord]) -> list[Issue]:
    """Block I: ID uniqueness across vault."""
    issues: list[Issue] = []
    seen_ids: dict[str, str] = {}  # id -> file path

    for note in notes:
        note_id = note.frontmatter.get("id")
        if not note_id:
            continue
        rel = str(note.path)
        if note_id in seen_ids:
            issues.append(Issue(
                severity=Severity.ERROR, block="I", file=rel,
                message=f"Duplicate ID '{note_id}' — also used in {seen_ids[note_id]}",
            ))
        else:
            seen_ids[note_id] = rel

    return issues


# ---------------------------------------------------------------------------
# Block J — Status hygiene
# ---------------------------------------------------------------------------

def check_block_j(note: NoteRecord) -> list[Issue]:
    """Block J: Status hygiene."""
    rel = str(note.path)
    issues: list[Issue] = []
    fm = note.frontmatter
    body = note.body

    if not fm:
        return issues

    status = fm.get("status", "")

    if status == "needs-update":
        needs_attention = fm.get("needs_attention")
        if not needs_attention:
            issues.append(Issue(
                severity=Severity.INFO, block="J", file=rel,
                message="Status 'needs-update' should have 'needs_attention:' flag explaining what needs updating",
            ))

    if status == "archived":
        # Check body for supersedes:: link
        typed_rels = extract_typed_relations(body)
        has_supersedes = any(r == "supersedes" for r, _ in typed_rels)
        # Also check frontmatter supersedes field
        fm_supersedes = fm.get("supersedes")
        if not has_supersedes and not fm_supersedes:
            issues.append(Issue(
                severity=Severity.INFO, block="J", file=rel,
                message="Status 'archived' should have 'supersedes::' link to successor (or supersedes: in frontmatter)",
            ))

    if status == "contested":
        # Should link to a debate note
        typed_rels = extract_typed_relations(body)
        has_position_in = any(r == "position-in" for r, _ in typed_rels)
        if not has_position_in:
            issues.append(Issue(
                severity=Severity.INFO, block="J", file=rel,
                message="Status 'contested' should link to a debate note via 'position-in::' or contain debate structure",
            ))

    return issues


# ---------------------------------------------------------------------------
# Block K — Agent identity resolution
# ---------------------------------------------------------------------------

def check_block_k(
    note: NoteRecord, agent_ids: set[str], agents_folder_exists: bool
) -> list[Issue]:
    """Block K: Forum-tier agent_id resolves to a registered Agent profile."""
    rel = str(note.path)
    issues: list[Issue] = []
    fm = note.frontmatter

    if not fm:
        return issues

    note_type = fm.get("type", "")

    if note_type not in FORUM_TYPES:
        return issues

    agent_id = fm.get("agent_id")
    if not agent_id:
        issues.append(Issue(
            severity=Severity.ERROR, block="K", file=rel,
            message=f"Forum-tier note (type: {note_type}) missing 'agent_id' field",
        ))
        return issues

    # Phase-0 exception: if no Agents/ folder exists, emit WARN not ERROR
    if not agents_folder_exists:
        issues.append(Issue(
            severity=Severity.WARN, block="K", file=rel,
            message=f"'agent_id' = '{agent_id}' cannot be resolved — no Agents/ folder exists",
        ))
        return issues

    if agent_id not in agent_ids:
        issues.append(Issue(
            severity=Severity.ERROR, block="K", file=rel,
            message=f"'agent_id' = '{agent_id}' does not resolve to any agent profile in Agents/",
        ))

    return issues


# ---------------------------------------------------------------------------
# Block L — Forum relationship well-formedness
# ---------------------------------------------------------------------------

def check_block_l(
    note: NoteRecord, id_to_path: dict[str, Path],
    filename_to_id: dict[str, str], agent_ids: set[str],
    agents_folder_exists: bool
) -> list[Issue]:
    """Block L: Forum relationship well-formedness."""
    rel = str(note.path)
    issues: list[Issue] = []
    fm = note.frontmatter
    body = note.body

    if not fm:
        return issues

    note_type = fm.get("type", "")
    status = fm.get("status", "")
    agent_id = fm.get("agent_id", "")

    # Severity: ERROR for reviewed, WARN for draft
    sev = Severity.ERROR if status == "reviewed" else Severity.WARN

    typed_rels = extract_typed_relations(body)
    rel_map: dict[str, list[str]] = {}
    for r, t in typed_rels:
        rel_map.setdefault(r, []).append(t)

    def target_exists(target: str) -> bool:
        target_clean = target.strip()
        return (
            target_clean in id_to_path
            or _slugify(target_clean) in id_to_path
            or target_clean in filename_to_id
        )

    def target_has_type(target: str, expected_types: set[str]) -> bool:
        """Check if a target note has one of the expected types."""
        for record_path, path_obj in id_to_path.items():
            if record_path == target or record_path == _slugify(target):
                # Load the target's frontmatter
                try:
                    raw = path_obj.read_text(encoding="utf-8")
                    fm2, _, _ = parse_frontmatter(raw, str(path_obj))
                    if fm2 and fm2.get("type") in expected_types:
                        return True
                except Exception:
                    pass
                return False
        # Try filename_to_id resolution
        note_id = filename_to_id.get(target)
        if note_id and note_id in id_to_path:
            try:
                raw = id_to_path[note_id].read_text(encoding="utf-8")
                fm2, _, _ = parse_frontmatter(raw, str(id_to_path[note_id]))
                if fm2 and fm2.get("type") in expected_types:
                    return True
            except Exception:
                pass
        return False

    if note_type in ("post", "reply"):
        # Must have posted-by:: [[agent-id]] in body
        posted_by_targets = rel_map.get("posted-by", [])
        if not posted_by_targets:
            issues.append(Issue(
                severity=sev, block="L", file=rel,
                message=f"Type '{note_type}' body must contain 'posted-by:: [[<agent>]]'",
            ))
        else:
            # posted-by target should match agent_id
            pb_target = posted_by_targets[0].strip()
            if agent_id and pb_target != agent_id and _slugify(pb_target) != _slugify(agent_id):
                issues.append(Issue(
                    severity=sev, block="L", file=rel,
                    message=f"'posted-by:: [[{pb_target}]]' does not match 'agent_id: {agent_id}'",
                ))

    if note_type == "reply":
        # replies_to: frontmatter field
        replies_to_fm = fm.get("replies_to")
        if not replies_to_fm:
            issues.append(Issue(
                severity=sev, block="L", file=rel,
                message="Reply missing 'replies_to:' frontmatter field",
            ))
        else:
            # Extract target from wikilink if needed
            wl_match = WIKILINK_PATTERN.search(str(replies_to_fm))
            target = wl_match.group(1) if wl_match else str(replies_to_fm).strip()
            if not target_exists(target):
                issues.append(Issue(
                    severity=sev, block="L", file=rel,
                    message=f"'replies_to: [[{target}]]' target not found in vault",
                ))

        # in_thread: frontmatter field
        in_thread_fm = fm.get("in_thread")
        if not in_thread_fm:
            issues.append(Issue(
                severity=sev, block="L", file=rel,
                message="Reply missing 'in_thread:' frontmatter field",
            ))
        else:
            wl_match = WIKILINK_PATTERN.search(str(in_thread_fm))
            target = wl_match.group(1) if wl_match else str(in_thread_fm).strip()
            if not target_exists(target):
                issues.append(Issue(
                    severity=sev, block="L", file=rel,
                    message=f"'in_thread: [[{target}]]' target not found in vault",
                ))

        # Body must have replies-to:: and in-thread::
        if "replies-to" not in rel_map:
            issues.append(Issue(
                severity=sev, block="L", file=rel,
                message="Reply body must contain 'replies-to:: [[<post>]]'",
            ))
        if "in-thread" not in rel_map:
            issues.append(Issue(
                severity=sev, block="L", file=rel,
                message="Reply body must contain 'in-thread:: [[<thread>]]'",
            ))

    if note_type == "thread":
        # seed_post (optional) — if present, target must exist and be type:post
        seed_post = fm.get("seed_post")
        if seed_post:
            wl_match = WIKILINK_PATTERN.search(str(seed_post))
            target = wl_match.group(1) if wl_match else str(seed_post).strip()
            if not target_exists(target):
                issues.append(Issue(
                    severity=sev, block="L", file=rel,
                    message=f"'seed_post: [[{target}]]' target not found in vault",
                ))

        # participants must be valid agent_ids
        participants = fm.get("participants", [])
        if isinstance(participants, list):
            for p in participants:
                if agents_folder_exists and p not in agent_ids:
                    issues.append(Issue(
                        severity=sev, block="L", file=rel,
                        message=f"Thread participant '{p}' does not resolve to an Agents/ profile",
                    ))

    return issues


# ---------------------------------------------------------------------------
# Main validation runner
# ---------------------------------------------------------------------------

@dataclass
class ValidationReport:
    issues: list[Issue] = field(default_factory=list)

    def add(self, issue_or_issues: Issue | list[Issue]) -> None:
        if isinstance(issue_or_issues, list):
            self.issues.extend(issue_or_issues)
        else:
            self.issues.append(issue_or_issues)

    @property
    def errors(self) -> list[Issue]:
        return [i for i in self.issues if i.severity == Severity.ERROR]

    @property
    def warns(self) -> list[Issue]:
        return [i for i in self.issues if i.severity == Severity.WARN]

    @property
    def infos(self) -> list[Issue]:
        return [i for i in self.issues if i.severity == Severity.INFO]

    def exit_code(self, strict: bool = False) -> int:
        if self.errors:
            return 2
        if strict and self.warns:
            return 1
        if self.warns:
            return 1
        return 0


def build_lookup_maps(notes: list[NoteRecord]) -> tuple[dict[str, Path], dict[str, str], set[str], bool]:
    """
    Build lookup maps for resolution:
    - id_to_path: note_id -> Path
    - filename_to_id: filename (without .md) -> note_id
    - agent_ids: set of known agent_id values
    - agents_folder_exists: bool
    """
    id_to_path: dict[str, Path] = {}
    filename_to_id: dict[str, str] = {}
    agent_ids: set[str] = set()
    agents_folder_exists = False

    for note in notes:
        fm = note.frontmatter
        if not fm:
            continue
        note_id = fm.get("id")
        if note_id:
            id_to_path[str(note_id)] = note.path

        # Map filename (without .md) to id for wikilink resolution
        stem = note.path.stem
        if note_id:
            filename_to_id[stem] = str(note_id)

        # Collect agent IDs
        if fm.get("type") == "agent":
            aid = fm.get("agent_id")
            if aid:
                agent_ids.add(str(aid))
            # Also track folder existence
            if "Agents" in str(note.path):
                agents_folder_exists = True

    return id_to_path, filename_to_id, agent_ids, agents_folder_exists


def validate_notes(notes: list[NoteRecord], vault_root: Path) -> ValidationReport:
    """Run all 12 validation blocks on a list of notes."""
    report = ValidationReport()

    if not notes:
        return report

    # Build lookup maps (needed for F, K, L)
    id_to_path, filename_to_id, agent_ids, agents_folder_exists = build_lookup_maps(notes)

    # Per-note blocks
    for note in notes:
        rel = str(note.path.relative_to(vault_root))
        note.path = note.path  # keep absolute

        # Re-build relative path for display
        try:
            display_path = str(note.path.relative_to(vault_root))
        except ValueError:
            display_path = str(note.path)

        # Patch issue file paths to relative
        def run_block(block_fn, *args, **kwargs):
            issues = block_fn(*args, **kwargs)
            for issue in issues:
                issue.file = display_path
            return issues

        report.add(run_block(check_block_a, note))
        if not note.frontmatter:
            # Can't run further checks if no frontmatter
            continue
        report.add(run_block(check_block_b, note))
        report.add(run_block(check_block_c, note))
        report.add(run_block(check_block_d, note))
        report.add(run_block(check_block_e, note))
        report.add(run_block(check_block_f, note, id_to_path, filename_to_id))
        report.add(run_block(check_block_g, note))
        report.add(run_block(check_block_h, note))
        report.add(run_block(check_block_j, note))
        report.add(run_block(check_block_k, note, agent_ids, agents_folder_exists))
        report.add(run_block(check_block_l, note, id_to_path, filename_to_id, agent_ids, agents_folder_exists))

    # Cross-note blocks
    report.add(check_block_i(notes))

    return report


# ---------------------------------------------------------------------------
# Output formatting
# ---------------------------------------------------------------------------

def format_human(report: ValidationReport, quiet: bool = False) -> str:
    """Format report as human-readable text."""
    lines: list[str] = []

    total = len(report.issues)
    errors = len(report.errors)
    warns = len(report.warns)
    infos = len(report.infos)

    lines.append("=" * 72)
    lines.append("The Nest — Schema Validation Report")
    lines.append("=" * 72)
    lines.append(f"Total issues: {total}  |  ERROR: {errors}  |  WARN: {warns}  |  INFO: {infos}")
    lines.append("")

    if not quiet:
        # Per-block summary
        block_counts: dict[str, dict[str, int]] = {}
        for issue in report.issues:
            if issue.block not in block_counts:
                block_counts[issue.block] = {"ERROR": 0, "WARN": 0, "INFO": 0}
            block_counts[issue.block][issue.severity] += 1

        if block_counts:
            lines.append("Block summary:")
            for block in sorted(block_counts.keys(), key=lambda b: (len(b), b)):
                bc = block_counts[block]
                lines.append(
                    f"  Block {block}: "
                    f"ERROR={bc['ERROR']} WARN={bc['WARN']} INFO={bc['INFO']}"
                )
            lines.append("")

    # Per-file issues
    if quiet:
        show_issues = [i for i in report.issues if i.severity == Severity.ERROR]
    else:
        show_issues = report.issues

    if show_issues:
        # Group by file
        by_file: dict[str, list[Issue]] = {}
        for issue in show_issues:
            by_file.setdefault(issue.file, []).append(issue)

        for file_path in sorted(by_file.keys()):
            file_issues = by_file[file_path]
            lines.append(f"  {file_path}")
            for issue in file_issues:
                loc = f" (line {issue.line})" if issue.line else ""
                lines.append(f"    [{issue.severity}] Block {issue.block}{loc}: {issue.message}")
            lines.append("")

    if errors == 0 and warns == 0:
        lines.append("✓ No ERROR or WARN issues found.")
    elif errors == 0:
        lines.append(f"✓ No ERROR issues. {warns} WARN(s) logged.")
    else:
        lines.append(f"✗ {errors} ERROR(s) found — fix before commit.")

    lines.append("=" * 72)
    return "\n".join(lines)


def format_json(report: ValidationReport) -> str:
    """Format report as JSON."""
    data = {
        "summary": {
            "total": len(report.issues),
            "error": len(report.errors),
            "warn": len(report.warns),
            "info": len(report.infos),
        },
        "issues": [i.to_dict() for i in report.issues],
    }
    return json.dumps(data, indent=2)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def find_vault_root(start: Path) -> Path:
    """Walk up from start to find the vault root (contains _Schema/ and _Meta/)."""
    candidate = start
    for _ in range(10):
        if (candidate / "_Schema").exists() and (candidate / "_Meta").exists():
            return candidate
        parent = candidate.parent
        if parent == candidate:
            break
        candidate = parent
    return start


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate The Nest vault against schema rules (Blocks A–L).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exit codes:
  0  Clean (no WARN or ERROR), or INFO-only issues
  1  WARN-level issues found
  2  ERROR-level issues found

Examples:
  python scripts/validate.py --all
  python scripts/validate.py --all --strict --json
  python scripts/validate.py --file Concepts/AI\\ Alignment.md
  python scripts/validate.py --all --quiet
        """,
    )
    parser.add_argument(
        "--all", action="store_true",
        help="Scan the entire vault (default if no --file given)",
    )
    parser.add_argument(
        "--file", metavar="PATH",
        help="Validate a single file",
    )
    parser.add_argument(
        "--strict", action="store_true",
        help="Treat WARN as ERROR (exit code 1 on WARN)",
    )
    parser.add_argument(
        "--json", action="store_true",
        help="Machine-readable JSON output",
    )
    parser.add_argument(
        "--quiet", action="store_true",
        help="Errors only — suppress WARN and INFO in output",
    )
    parser.add_argument(
        "--vault-root", metavar="DIR",
        help="Path to vault root (auto-detected if omitted)",
    )

    args = parser.parse_args()

    # Determine vault root
    if args.vault_root:
        vault_root = Path(args.vault_root).resolve()
    else:
        vault_root = find_vault_root(Path.cwd())

    if not vault_root.exists():
        print(f"ERROR: vault root not found: {vault_root}", file=sys.stderr)
        sys.exit(2)

    # Load notes
    if args.file:
        file_path = Path(args.file).resolve()
        if not file_path.exists():
            print(f"ERROR: file not found: {file_path}", file=sys.stderr)
            sys.exit(2)
        notes = load_single_file(file_path, vault_root)
        # For single file, still load whole vault for cross-note checks
        all_notes = load_vault(vault_root)
        # Replace matching note in all_notes with the one we want to validate
        file_notes = load_single_file(file_path, vault_root)
        # Validate using the full vault for lookups but report only the single file
        report_all = validate_notes(all_notes, vault_root)
        rel_target = str(file_path.relative_to(vault_root))
        # Filter to only issues for the target file
        filtered = ValidationReport()
        filtered.issues = [i for i in report_all.issues if i.file == rel_target]
        # Also include cross-note issues
        for i in report_all.issues:
            if i.block == "I" and rel_target in i.message:
                if i not in filtered.issues:
                    filtered.issues.append(i)
        report = filtered
    else:
        # Default: --all
        notes = load_vault(vault_root)
        report = validate_notes(notes, vault_root)

    # Output
    if args.json:
        print(format_json(report))
    else:
        print(format_human(report, quiet=args.quiet))

    sys.exit(report.exit_code(strict=args.strict))


if __name__ == "__main__":
    main()
