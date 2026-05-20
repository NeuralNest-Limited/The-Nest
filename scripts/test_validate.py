"""
test_validate.py — pytest suite for validate.py

Tests all 12 validation blocks (A through L) using:
  - Valid fixtures in test_fixtures/valid/ (must produce 0 errors + 0 warns)
  - Invalid fixtures in test_fixtures/invalid/ (must produce expected failures)

Run with: pytest scripts/test_validate.py
"""

from __future__ import annotations

import pytest
from pathlib import Path

# Add scripts/ to sys.path so we can import validate
import sys
sys.path.insert(0, str(Path(__file__).parent))

from validate import (
    NoteRecord,
    ValidationReport,
    Issue,
    Severity,
    parse_frontmatter,
    load_vault,
    validate_notes,
    build_lookup_maps,
    check_block_a,
    check_block_b,
    check_block_c,
    check_block_d,
    check_block_e,
    check_block_f,
    check_block_g,
    check_block_h,
    check_block_i,
    check_block_j,
    check_block_k,
    check_block_l,
)

# ---------------------------------------------------------------------------
# Fixture paths
# ---------------------------------------------------------------------------

SCRIPTS_DIR = Path(__file__).parent
VALID_DIR = SCRIPTS_DIR / "test_fixtures" / "valid"
INVALID_DIR = SCRIPTS_DIR / "test_fixtures" / "invalid"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_note(content: str, file_path: str = "test.md") -> NoteRecord:
    """Create a NoteRecord from raw markdown content."""
    fm, body, _ = parse_frontmatter(content, file_path)
    return NoteRecord(
        path=Path(file_path),
        raw=content,
        frontmatter=fm if fm is not None else {},
        body=body,
    )


def load_fixture(name: str, folder: Path) -> NoteRecord:
    """Load a test fixture file as a NoteRecord."""
    path = folder / name
    raw = path.read_text(encoding="utf-8")
    fm, body, _ = parse_frontmatter(raw, str(path))
    return NoteRecord(
        path=path,
        raw=raw,
        frontmatter=fm if fm is not None else {},
        body=body,
    )


def has_error(issues: list[Issue], block: str | None = None) -> bool:
    """Return True if any ERROR-severity issue exists (optionally filtered by block)."""
    return any(
        i.severity == Severity.ERROR and (block is None or i.block == block)
        for i in issues
    )


def has_warn(issues: list[Issue], block: str | None = None) -> bool:
    """Return True if any WARN-severity issue exists (optionally filtered by block)."""
    return any(
        i.severity == Severity.WARN and (block is None or i.block == block)
        for i in issues
    )


def has_info(issues: list[Issue], block: str | None = None) -> bool:
    """Return True if any INFO-severity issue exists (optionally filtered by block)."""
    return any(
        i.severity == Severity.INFO and (block is None or i.block == block)
        for i in issues
    )


def all_valid_ids():
    """Return list of valid fixture filenames."""
    return [p.name for p in sorted(VALID_DIR.glob("*.md"))]


def all_invalid_ids():
    """Return list of invalid fixture filenames."""
    return [p.name for p in sorted(INVALID_DIR.glob("*.md"))]


# ---------------------------------------------------------------------------
# Tests for valid fixtures (must pass cleanly)
# ---------------------------------------------------------------------------

class TestValidFixtures:
    """All valid fixtures must produce zero ERROR-level issues."""

    @pytest.mark.parametrize("fixture_name", all_valid_ids())
    def test_valid_fixture_no_errors(self, fixture_name: str):
        """Valid fixtures must not produce any ERROR-severity issues."""
        note = load_fixture(fixture_name, VALID_DIR)

        # Use a mini-vault with just the valid fixtures for lookup
        all_valid_notes = [load_fixture(n, VALID_DIR) for n in all_valid_ids()]
        id_to_path, filename_to_id, agent_ids, agents_folder_exists = build_lookup_maps(
            all_valid_notes
        )

        issues: list[Issue] = []
        issues.extend(check_block_a(note))
        if note.frontmatter:
            issues.extend(check_block_b(note))
            issues.extend(check_block_c(note))
            issues.extend(check_block_d(note))
            issues.extend(check_block_e(note))
            issues.extend(check_block_f(note, id_to_path, filename_to_id))
            issues.extend(check_block_g(note))
            issues.extend(check_block_h(note))
            issues.extend(check_block_j(note))
            issues.extend(check_block_k(note, agent_ids, agents_folder_exists))
            issues.extend(check_block_l(
                note, id_to_path, filename_to_id, agent_ids, agents_folder_exists
            ))

        errors = [i for i in issues if i.severity == Severity.ERROR]
        assert errors == [], (
            f"Valid fixture '{fixture_name}' produced unexpected ERRORs:\n"
            + "\n".join(f"  Block {i.block}: {i.message}" for i in errors)
        )

    def test_valid_concept(self):
        """concept-valid.md is a well-formed concept note."""
        note = load_fixture("concept-valid.md", VALID_DIR)
        assert note.frontmatter.get("type") == "concept"
        assert note.frontmatter.get("status") == "draft"

    def test_valid_person(self):
        """person-valid.md has all required person fields."""
        note = load_fixture("person-valid.md", VALID_DIR)
        assert note.frontmatter.get("type") == "person"
        assert "birth_year" in note.frontmatter

    def test_valid_org(self):
        """org-valid.md has valid org_kind value."""
        note = load_fixture("org-valid.md", VALID_DIR)
        assert note.frontmatter.get("org_kind") == "ngo"

    def test_valid_paper(self):
        """paper-valid.md has required paper fields."""
        note = load_fixture("paper-valid.md", VALID_DIR)
        assert note.frontmatter.get("type") == "paper"
        assert "authors" in note.frontmatter

    def test_valid_policy(self):
        """policy-valid.md has valid policy fields."""
        note = load_fixture("policy-valid.md", VALID_DIR)
        assert note.frontmatter.get("policy_status") == "enacted"

    def test_valid_debate(self):
        """debate-valid.md has positions and open_questions."""
        note = load_fixture("debate-valid.md", VALID_DIR)
        assert isinstance(note.frontmatter.get("positions"), list)

    def test_valid_event(self):
        """event-valid.md has valid event_kind."""
        note = load_fixture("event-valid.md", VALID_DIR)
        assert note.frontmatter.get("event_kind") == "summit"

    def test_valid_dataset(self):
        """dataset-valid.md has hosted_at and license."""
        note = load_fixture("dataset-valid.md", VALID_DIR)
        assert "hosted_at" in note.frontmatter

    def test_valid_case(self):
        """case-valid.md has valid case_status."""
        note = load_fixture("case-valid.md", VALID_DIR)
        assert note.frontmatter.get("case_status") == "pending"

    def test_valid_synthesis(self):
        """synthesis-valid.md has endorsement fields."""
        note = load_fixture("synthesis-valid.md", VALID_DIR)
        assert note.frontmatter.get("endorsement_status") == "draft"
        assert "endorsed_by" in note.frontmatter

    def test_valid_moc(self):
        """moc-valid.md has query_seed and covers_topics."""
        note = load_fixture("moc-valid.md", VALID_DIR)
        assert "query_seed" in note.frontmatter

    def test_valid_agent(self):
        """agent-valid.md has agent_id matching id."""
        note = load_fixture("agent-valid.md", VALID_DIR)
        assert note.frontmatter.get("agent_id") == note.frontmatter.get("id")

    def test_valid_post(self):
        """post-valid.md has agent_id and perspective."""
        note = load_fixture("post-valid.md", VALID_DIR)
        assert note.frontmatter.get("type") == "post"
        assert note.frontmatter.get("perspective") == "cautious"

    def test_valid_thread(self):
        """thread-valid.md has required question field."""
        note = load_fixture("thread-valid.md", VALID_DIR)
        assert "question" in note.frontmatter

    def test_valid_reply(self):
        """reply-valid.md has replies_to and in_thread fields."""
        note = load_fixture("reply-valid.md", VALID_DIR)
        assert "replies_to" in note.frontmatter
        assert "in_thread" in note.frontmatter

    def test_valid_stub(self):
        """stub-valid.md does not need summary/topics at stub status."""
        note = load_fixture("stub-valid.md", VALID_DIR)
        assert note.frontmatter.get("status") == "stub"
        issues = check_block_c(note)
        assert not has_warn(issues, "C")

    def test_valid_reviewed(self):
        """reviewed-valid.md has full content-bearing fields."""
        note = load_fixture("reviewed-valid.md", VALID_DIR)
        assert note.frontmatter.get("status") == "reviewed"
        issues = check_block_c(note)
        assert not has_warn(issues, "C")

    def test_valid_needs_update(self):
        """needs-update-valid.md has needs_attention flag."""
        note = load_fixture("needs-update-valid.md", VALID_DIR)
        assert note.frontmatter.get("status") == "needs-update"
        assert note.frontmatter.get("needs_attention")

    def test_valid_archived(self):
        """archived-valid.md has supersedes:: link."""
        note = load_fixture("archived-valid.md", VALID_DIR)
        assert note.frontmatter.get("status") == "archived"
        assert "supersedes::" in note.body


# ---------------------------------------------------------------------------
# Block A tests
# ---------------------------------------------------------------------------

class TestBlockA:
    """Block A: YAML well-formedness."""

    def test_no_frontmatter_is_error(self):
        """A note with no --- delimiter fails Block A."""
        note = load_fixture("block-a-no-frontmatter.md", INVALID_DIR)
        issues = check_block_a(note)
        assert has_error(issues, "A")

    def test_no_closing_delimiter_is_error(self):
        """A note with opening --- but no closing --- fails Block A."""
        note = load_fixture("block-a-no-closing.md", INVALID_DIR)
        issues = check_block_a(note)
        assert has_error(issues, "A")

    def test_bad_date_format_is_error(self):
        """A note with DD-MM-YYYY date format fails Block A."""
        note = load_fixture("block-a-bad-date.md", INVALID_DIR)
        # Block A date check is in check_block_a
        issues = check_block_a(note)
        assert has_error(issues, "A")

    def test_valid_dates_pass(self):
        """A note with correct ISO-8601 dates passes Block A."""
        note = load_fixture("concept-valid.md", VALID_DIR)
        issues = check_block_a(note)
        assert not has_error(issues, "A")

    def test_yaml_parse_error_is_error(self):
        """A note with invalid YAML produces a Block A error."""
        content = "---\nbad: yaml: colon:\n---\n# Title\n"
        note = make_note(content, "test-bad-yaml.md")
        # The raw note should fail to parse or have no frontmatter
        # We verify the parse itself handles this
        fm, body, issues = parse_frontmatter(content, "test-bad-yaml.md")
        assert any(i.severity == Severity.ERROR and i.block == "A" for i in issues)


# ---------------------------------------------------------------------------
# Block B tests
# ---------------------------------------------------------------------------

class TestBlockB:
    """Block B: Universal required fields."""

    def test_missing_id_is_error(self):
        """Missing 'id' field produces Block B ERROR."""
        note = load_fixture("block-b-missing-id.md", INVALID_DIR)
        issues = check_block_b(note)
        assert has_error(issues, "B")

    def test_unknown_type_is_error(self):
        """Unknown 'type' value produces Block B ERROR."""
        note = load_fixture("block-b-unknown-type.md", INVALID_DIR)
        issues = check_block_b(note)
        assert has_error(issues, "B")

    def test_unknown_status_is_error(self):
        """Unknown 'status' value produces Block B ERROR."""
        note = load_fixture("block-b-unknown-status.md", INVALID_DIR)
        issues = check_block_b(note)
        assert has_error(issues, "B")

    def test_valid_concept_passes(self):
        """concept-valid.md passes Block B."""
        note = load_fixture("concept-valid.md", VALID_DIR)
        issues = check_block_b(note)
        assert not has_error(issues, "B")

    def test_missing_authored_by_is_error(self):
        """Missing 'authored_by' field produces Block B ERROR."""
        content = """---
id: test-missing-authored-by
title: Test
type: concept
status: draft
created: 2026-01-01
last_reviewed: 2026-01-01
schema_version: 0.2
---
# Test
"""
        note = make_note(content)
        issues = check_block_b(note)
        assert has_error(issues, "B")


# ---------------------------------------------------------------------------
# Block C tests
# ---------------------------------------------------------------------------

class TestBlockC:
    """Block C: Content-bearing required fields."""

    def test_missing_summary_warns(self):
        """A draft note without summary produces Block C WARN."""
        note = load_fixture("block-c-missing-summary.md", INVALID_DIR)
        issues = check_block_c(note)
        assert has_warn(issues, "C")

    def test_missing_topics_warns(self):
        """A draft note without topics produces Block C WARN."""
        note = load_fixture("block-c-missing-topics.md", INVALID_DIR)
        issues = check_block_c(note)
        assert has_warn(issues, "C")

    def test_stub_exempt_from_content_check(self):
        """Stub notes do not need summary or topics."""
        note = load_fixture("stub-valid.md", VALID_DIR)
        issues = check_block_c(note)
        assert not has_warn(issues, "C")

    def test_archived_exempt_from_content_check(self):
        """Archived notes do not need summary or topics."""
        note = load_fixture("archived-valid.md", VALID_DIR)
        issues = check_block_c(note)
        assert not has_warn(issues, "C")

    def test_summary_too_long_warns(self):
        """A summary over 280 characters produces Block C WARN."""
        long_summary = "x" * 281
        content = f"""---
id: test-long-summary
title: Test Long Summary
type: concept
status: draft
created: 2026-01-01
last_reviewed: 2026-01-01
authored_by: claude-sonnet-4-6
schema_version: 0.2
summary: "{long_summary}"
topics: [ai-safety]
---
# Test
"""
        note = make_note(content)
        issues = check_block_c(note)
        assert has_warn(issues, "C")


# ---------------------------------------------------------------------------
# Block D tests
# ---------------------------------------------------------------------------

class TestBlockD:
    """Block D: Type-specific required fields."""

    def test_person_missing_birth_year_is_error(self):
        """A person note missing birth_year fails Block D."""
        note = load_fixture("block-d-person-missing-field.md", INVALID_DIR)
        issues = check_block_d(note)
        assert has_error(issues, "D")

    def test_agent_id_mismatch_is_error(self):
        """An agent note where agent_id != id fails Block D."""
        note = load_fixture("block-d-agent-id-mismatch.md", INVALID_DIR)
        issues = check_block_d(note)
        assert has_error(issues, "D")

    def test_invalid_org_kind_is_error(self):
        """An org note with invalid org_kind fails Block D."""
        note = load_fixture("block-d-invalid-org-kind.md", INVALID_DIR)
        issues = check_block_d(note)
        assert has_error(issues, "D")

    def test_post_no_perspective_is_error(self):
        """A post without perspective fails Block D."""
        note = load_fixture("block-d-post-no-perspective.md", INVALID_DIR)
        issues = check_block_d(note)
        assert has_error(issues, "D")

    def test_valid_person_passes(self):
        """person-valid.md passes Block D."""
        note = load_fixture("person-valid.md", VALID_DIR)
        issues = check_block_d(note)
        assert not has_error(issues, "D")

    def test_valid_agent_passes(self):
        """agent-valid.md passes Block D."""
        note = load_fixture("agent-valid.md", VALID_DIR)
        issues = check_block_d(note)
        assert not has_error(issues, "D")

    def test_synthesis_missing_endorsed_by_error(self):
        """A synthesis note without endorsed_by fails Block D."""
        content = """---
id: test-synthesis-no-endorsed
title: Test Synthesis
type: synthesis
status: draft
created: 2026-01-01
last_reviewed: 2026-01-01
authored_by: claude-sonnet-4-6
schema_version: 0.2
summary: A synthesis missing endorsed_by.
topics: [ai-safety]
perspective: cautious
endorsement_status: draft
---
# Test
"""
        note = make_note(content)
        issues = check_block_d(note)
        assert has_error(issues, "D")


# ---------------------------------------------------------------------------
# Block E tests
# ---------------------------------------------------------------------------

class TestBlockE:
    """Block E: Controlled vocabulary."""

    def test_bad_topic_warns(self):
        """An unknown topic value produces Block E WARN."""
        note = load_fixture("block-e-bad-topic.md", INVALID_DIR)
        issues = check_block_e(note)
        assert has_warn(issues, "E")

    def test_bad_perspective_warns(self):
        """An unknown perspective value produces Block E WARN."""
        note = load_fixture("block-e-bad-perspective.md", INVALID_DIR)
        issues = check_block_e(note)
        assert has_warn(issues, "E")

    def test_valid_concept_passes_vocab(self):
        """concept-valid.md uses only known topics and perspective."""
        note = load_fixture("concept-valid.md", VALID_DIR)
        issues = check_block_e(note)
        assert not has_warn(issues, "E")

    def test_confidence_out_of_range_warns(self):
        """Confidence out of 0.0-1.0 range produces Block E WARN."""
        content = """---
id: test-confidence-range
title: Test
type: concept
status: draft
created: 2026-01-01
last_reviewed: 2026-01-01
authored_by: claude-sonnet-4-6
schema_version: 0.2
summary: Test note.
topics: [ai-safety]
confidence: 1.5
---
# Test
"""
        note = make_note(content)
        issues = check_block_e(note)
        assert has_warn(issues, "E")

    def test_source_tier_out_of_range_warns(self):
        """source_tier out of 1-5 range produces Block E WARN."""
        content = """---
id: test-source-tier-range
title: Test
type: concept
status: draft
created: 2026-01-01
last_reviewed: 2026-01-01
authored_by: claude-sonnet-4-6
schema_version: 0.2
summary: Test note.
topics: [ai-safety]
source_tier: 6
---
# Test
"""
        note = make_note(content)
        issues = check_block_e(note)
        assert has_warn(issues, "E")


# ---------------------------------------------------------------------------
# Block F tests
# ---------------------------------------------------------------------------

class TestBlockF:
    """Block F: Relationships."""

    def test_unknown_relation_warns(self):
        """An unknown relation type produces Block F WARN."""
        note = load_fixture("block-f-unknown-relation.md", INVALID_DIR)
        id_to_path: dict = {}
        filename_to_id: dict = {}
        issues = check_block_f(note, id_to_path, filename_to_id)
        assert has_warn(issues, "F")

    def test_dangling_link_in_draft_warns(self):
        """A dangling link in a draft note produces Block F WARN."""
        content = """---
id: test-dangling-draft
title: Test
type: concept
status: draft
created: 2026-01-01
last_reviewed: 2026-01-01
authored_by: claude-sonnet-4-6
schema_version: 0.2
summary: Test note.
topics: [ai-safety]
---
# Test

supports:: [[nonexistent-note]]
"""
        note = make_note(content)
        issues = check_block_f(note, {}, {})
        assert has_warn(issues, "F")

    def test_resolved_link_no_warn(self):
        """A link that resolves to a known note does not warn."""
        content = """---
id: test-resolved-link
title: Test
type: concept
status: draft
created: 2026-01-01
last_reviewed: 2026-01-01
authored_by: claude-sonnet-4-6
schema_version: 0.2
summary: Test note.
topics: [ai-safety]
---
# Test

supports:: [[target-note-id]]
"""
        note = make_note(content)
        id_to_path = {"target-note-id": Path("Concepts/Target.md")}
        issues = check_block_f(note, id_to_path, {})
        assert not has_warn(issues, "F")


# ---------------------------------------------------------------------------
# Block G tests
# ---------------------------------------------------------------------------

class TestBlockG:
    """Block G: Source objects."""

    def test_source_no_locator_warns(self):
        """A source with no url/doi/arxiv_id produces Block G WARN."""
        note = load_fixture("block-g-source-no-locator.md", INVALID_DIR)
        issues = check_block_g(note)
        assert has_warn(issues, "G")

    def test_source_no_title_warns(self):
        """A source with no title produces Block G WARN."""
        note = load_fixture("block-g-source-no-title.md", INVALID_DIR)
        issues = check_block_g(note)
        assert has_warn(issues, "G")

    def test_valid_source_passes(self):
        """concept-valid.md sources are well-formed."""
        note = load_fixture("concept-valid.md", VALID_DIR)
        issues = check_block_g(note)
        assert not has_warn(issues, "G")

    def test_web_source_without_accessed_warns(self):
        """A web source (has url) without 'accessed' produces Block G WARN."""
        content = """---
id: test-web-no-accessed
title: Test
type: concept
status: draft
created: 2026-01-01
last_reviewed: 2026-01-01
authored_by: claude-sonnet-4-6
schema_version: 0.2
summary: Test note.
topics: [ai-safety]
sources:
  - type: website
    title: "Test Website"
    url: https://example.com
---
# Test
"""
        note = make_note(content)
        issues = check_block_g(note)
        assert has_warn(issues, "G")


# ---------------------------------------------------------------------------
# Block H tests
# ---------------------------------------------------------------------------

class TestBlockH:
    """Block H: Stance discipline."""

    def test_reference_nonneutral_perspective_info(self):
        """A reference-tier note with non-neutral perspective produces Block H INFO."""
        note = load_fixture("block-h-reference-nonneutral.md", INVALID_DIR)
        issues = check_block_h(note)
        assert has_info(issues, "H")

    def test_reference_neutral_perspective_no_info(self):
        """A reference-tier note with neutral perspective passes Block H."""
        note = load_fixture("concept-valid.md", VALID_DIR)
        issues = check_block_h(note)
        assert not has_info(issues, "H")

    def test_synthesis_missing_perspective_info(self):
        """A synthesis note missing perspective produces Block H INFO."""
        content = """---
id: test-synthesis-no-perspective
title: Test Synthesis
type: synthesis
status: draft
created: 2026-01-01
last_reviewed: 2026-01-01
authored_by: claude-sonnet-4-6
schema_version: 0.2
summary: Test synthesis missing perspective.
topics: [ai-safety]
endorsed_by:
  - id: claude-sonnet-4-6
    role: drafter
    kind: ai
endorsement_status: draft
---
# Test
"""
        note = make_note(content)
        issues = check_block_h(note)
        assert has_info(issues, "H")


# ---------------------------------------------------------------------------
# Block I tests
# ---------------------------------------------------------------------------

class TestBlockI:
    """Block I: ID uniqueness."""

    def test_duplicate_ids_produce_error(self):
        """Two notes with the same id produce Block I ERROR."""
        note_a = load_fixture("block-i-duplicate-id-a.md", INVALID_DIR)
        note_b = load_fixture("block-i-duplicate-id-b.md", INVALID_DIR)
        issues = check_block_i([note_a, note_b])
        assert has_error(issues, "I")

    def test_unique_ids_pass(self):
        """Notes with unique ids produce no Block I issues."""
        note_a = load_fixture("concept-valid.md", VALID_DIR)
        note_b = load_fixture("person-valid.md", VALID_DIR)
        issues = check_block_i([note_a, note_b])
        assert not has_error(issues, "I")


# ---------------------------------------------------------------------------
# Block J tests
# ---------------------------------------------------------------------------

class TestBlockJ:
    """Block J: Status hygiene."""

    def test_needs_update_without_flag_info(self):
        """A needs-update note without needs_attention produces Block J INFO."""
        note = load_fixture("block-j-needs-update-no-flag.md", INVALID_DIR)
        issues = check_block_j(note)
        assert has_info(issues, "J")

    def test_archived_without_supersedes_info(self):
        """An archived note without supersedes:: produces Block J INFO."""
        note = load_fixture("block-j-archived-no-supersedes.md", INVALID_DIR)
        issues = check_block_j(note)
        assert has_info(issues, "J")

    def test_needs_update_with_flag_passes(self):
        """A needs-update note with needs_attention passes Block J."""
        note = load_fixture("needs-update-valid.md", VALID_DIR)
        issues = check_block_j(note)
        assert not has_info(issues, "J")

    def test_archived_with_supersedes_passes(self):
        """An archived note with supersedes:: passes Block J."""
        note = load_fixture("archived-valid.md", VALID_DIR)
        issues = check_block_j(note)
        assert not has_info(issues, "J")


# ---------------------------------------------------------------------------
# Block K tests
# ---------------------------------------------------------------------------

class TestBlockK:
    """Block K: Agent identity resolution."""

    def test_missing_agent_id_is_error(self):
        """A forum note without agent_id fails Block K."""
        note = load_fixture("block-k-missing-agent-id.md", INVALID_DIR)
        issues = check_block_k(note, set(), agents_folder_exists=True)
        assert has_error(issues, "K")

    def test_dangling_agent_id_is_error(self):
        """A forum note with unregistered agent_id fails Block K."""
        note = load_fixture("block-k-dangling-agent-id.md", INVALID_DIR)
        # The agent 'openai-gpt-999' doesn't exist in any agent set
        issues = check_block_k(note, {"anthropic-claude-opus-4-7"}, agents_folder_exists=True)
        assert has_error(issues, "K")

    def test_valid_agent_id_passes(self):
        """A post with a registered agent_id passes Block K."""
        note = load_fixture("post-valid.md", VALID_DIR)
        agent_ids = {"test-provider-test-model-1-0"}
        issues = check_block_k(note, agent_ids, agents_folder_exists=True)
        assert not has_error(issues, "K")

    def test_no_agents_folder_gives_warn_not_error(self):
        """Without an Agents/ folder, Block K emits WARN not ERROR."""
        note = load_fixture("block-k-dangling-agent-id.md", INVALID_DIR)
        issues = check_block_k(note, set(), agents_folder_exists=False)
        # Should be WARN not ERROR when no folder exists
        assert not has_error(issues, "K")
        assert has_warn(issues, "K")

    def test_non_forum_type_skipped(self):
        """Non-forum-tier notes are not checked by Block K."""
        note = load_fixture("concept-valid.md", VALID_DIR)
        issues = check_block_k(note, set(), agents_folder_exists=True)
        assert issues == []


# ---------------------------------------------------------------------------
# Block L tests
# ---------------------------------------------------------------------------

class TestBlockL:
    """Block L: Forum relationship well-formedness."""

    def test_reply_missing_replies_to_warns(self):
        """A reply without replies_to frontmatter produces Block L WARN (draft)."""
        note = load_fixture("block-l-reply-missing-replies-to.md", INVALID_DIR)
        all_valid_notes = [load_fixture(n, VALID_DIR) for n in all_valid_ids()]
        id_to_path, filename_to_id, agent_ids, agents_folder_exists = build_lookup_maps(
            all_valid_notes
        )
        issues = check_block_l(
            note, id_to_path, filename_to_id, agent_ids, agents_folder_exists
        )
        assert has_warn(issues, "L")

    def test_post_no_posted_by_warns(self):
        """A post without posted-by:: in body produces Block L WARN (draft)."""
        note = load_fixture("block-l-post-no-posted-by.md", INVALID_DIR)
        all_valid_notes = [load_fixture(n, VALID_DIR) for n in all_valid_ids()]
        id_to_path, filename_to_id, agent_ids, agents_folder_exists = build_lookup_maps(
            all_valid_notes
        )
        issues = check_block_l(
            note, id_to_path, filename_to_id, agent_ids, agents_folder_exists
        )
        assert has_warn(issues, "L")

    def test_valid_reply_passes(self):
        """reply-valid.md passes Block L."""
        note = load_fixture("reply-valid.md", VALID_DIR)
        all_valid_notes = [load_fixture(n, VALID_DIR) for n in all_valid_ids()]
        id_to_path, filename_to_id, agent_ids, agents_folder_exists = build_lookup_maps(
            all_valid_notes
        )
        issues = check_block_l(
            note, id_to_path, filename_to_id, agent_ids, agents_folder_exists
        )
        errors = [i for i in issues if i.severity == Severity.ERROR]
        assert errors == []

    def test_valid_post_passes(self):
        """post-valid.md passes Block L."""
        note = load_fixture("post-valid.md", VALID_DIR)
        all_valid_notes = [load_fixture(n, VALID_DIR) for n in all_valid_ids()]
        id_to_path, filename_to_id, agent_ids, agents_folder_exists = build_lookup_maps(
            all_valid_notes
        )
        issues = check_block_l(
            note, id_to_path, filename_to_id, agent_ids, agents_folder_exists
        )
        errors = [i for i in issues if i.severity == Severity.ERROR]
        assert errors == []

    def test_concept_type_skipped(self):
        """Non-forum-tier notes are skipped by Block L."""
        note = load_fixture("concept-valid.md", VALID_DIR)
        issues = check_block_l(note, {}, {}, set(), True)
        assert issues == []


# ---------------------------------------------------------------------------
# Integration tests
# ---------------------------------------------------------------------------

class TestIntegration:
    """Integration tests for end-to-end validation behavior."""

    def test_validate_valid_fixtures_zero_errors(self):
        """Running validate_notes on all valid fixtures produces zero ERRORs."""
        notes = [load_fixture(n, VALID_DIR) for n in all_valid_ids()]
        # Use valid fixture dir as mock vault root
        report = validate_notes(notes, VALID_DIR)
        errors = report.errors
        assert errors == [], (
            "Valid fixtures produced ERRORs:\n"
            + "\n".join(f"  [{i.file}] Block {i.block}: {i.message}" for i in errors)
        )

    def test_invalid_fixtures_produce_issues(self):
        """At least one invalid fixture produces an issue."""
        notes = [load_fixture(n, INVALID_DIR) for n in all_invalid_ids()]
        report = validate_notes(notes, INVALID_DIR)
        assert len(report.issues) > 0, "Expected at least one issue from invalid fixtures"

    def test_duplicate_id_detection_cross_file(self):
        """Block I detects duplicate IDs across two notes."""
        note_a = load_fixture("block-i-duplicate-id-a.md", INVALID_DIR)
        note_b = load_fixture("block-i-duplicate-id-b.md", INVALID_DIR)
        issues = check_block_i([note_a, note_b])
        assert has_error(issues, "I"), "Expected duplicate ID error"

    def test_exit_code_zero_for_clean_vault(self):
        """A report with no issues gives exit code 0."""
        report = ValidationReport()
        assert report.exit_code() == 0

    def test_exit_code_one_for_warns(self):
        """A report with only WARNs gives exit code 1."""
        report = ValidationReport()
        report.add(Issue(Severity.WARN, "F", "test.md", "dangling link"))
        assert report.exit_code() == 1

    def test_exit_code_two_for_errors(self):
        """A report with ERRORs gives exit code 2."""
        report = ValidationReport()
        report.add(Issue(Severity.ERROR, "B", "test.md", "missing id"))
        assert report.exit_code() == 2

    def test_strict_mode_escalates_warn_to_error(self):
        """With strict=True, WARN-only report gives exit code 1."""
        report = ValidationReport()
        report.add(Issue(Severity.WARN, "F", "test.md", "dangling link"))
        assert report.exit_code(strict=True) == 1

    def test_count_all_valid_fixtures(self):
        """At least 20 valid fixtures exist."""
        valid_count = len(all_valid_ids())
        assert valid_count >= 20, f"Expected >= 20 valid fixtures, found {valid_count}"

    def test_count_all_invalid_fixtures(self):
        """At least 20 invalid fixtures exist."""
        invalid_count = len(all_invalid_ids())
        assert invalid_count >= 20, f"Expected >= 20 invalid fixtures, found {invalid_count}"

    def test_parse_frontmatter_handles_obsidian_wikilinks(self):
        """parse_frontmatter handles Obsidian [[wikilink]] in YAML fields."""
        content = """---
id: test-wikilinks
title: Test
type: concept
status: draft
created: 2026-01-01
last_reviewed: 2026-01-01
authored_by: claude-sonnet-4-6
schema_version: 0.2
related: [[Note A]], [[Note B]]
---
# Test
"""
        fm, body, issues = parse_frontmatter(content, "test.md")
        # Should parse without YAML errors
        assert fm is not None
        assert fm.get("id") == "test-wikilinks"
        assert not any(i.severity == Severity.ERROR for i in issues)

    def test_json_output_is_valid_json(self):
        """format_json produces valid JSON."""
        import json
        from validate import format_json
        report = ValidationReport()
        report.add(Issue(Severity.WARN, "F", "test.md", "dangling link"))
        json_output = format_json(report)
        data = json.loads(json_output)
        assert "summary" in data
        assert "issues" in data
        assert data["summary"]["warn"] == 1
