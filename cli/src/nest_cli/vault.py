"""Vault discovery and common vault operations.

A *vault* is a directory containing The Nest's content: at minimum it
must hold a ``_Schema/`` folder, a ``_Meta/`` folder, and a
``_Templates/`` folder. Optionally a marker file ``.nest-vault`` may sit
at the root for explicit identification.

Discovery walks upward from a starting path, looking for the markers.
This mirrors the heuristic used by ``scripts/validate.py`` so that the
CLI and the validator agree on what counts as a vault.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

VAULT_MARKER_FILE = ".nest-vault"
REQUIRED_SUBDIRS = ("_Schema", "_Meta", "_Templates")

# Folder per note type (matches scripts/validate.py CONTENT_FOLDERS plus
# the canonical Concept folder set from _Schema/Note Types.md).
TYPE_TO_FOLDER: dict[str, str] = {
    "concept": "Concepts",
    "person": "People",
    "org": "Organizations",
    "paper": "Papers",
    "policy": "Policies",
    "debate": "Debates",
    "event": "Events",
    "dataset": "Datasets",
    "case": "Cases",
    "synthesis": "_Synthesis",
    "moc": "_Indexes",
    "schema": "_Schema",
    "meta": "_Meta",
    "post": "Forum",
    "thread": "Forum",
    "reply": "Forum",
    "agent": "Agents",
}

# Reverse: template filename pattern per type
TYPE_TO_TEMPLATE: dict[str, str] = {
    "concept": "Concept Template.md",
    "person": "Person Template.md",
    "org": "Organization Template.md",
    "paper": "Paper Template.md",
    "policy": "Policy Template.md",
    "debate": "Debate Template.md",
    "event": "Event Template.md",
    "dataset": "Dataset Template.md",
    "case": "Case Template.md",
    "synthesis": "Synthesis Template.md",
    "moc": "MOC Template.md",
    "post": "Post Template.md",
    "thread": "Thread Template.md",
    "reply": "Reply Template.md",
    "agent": "Agent Template.md",
}


class VaultNotFoundError(RuntimeError):
    """Raised when no vault can be discovered from a starting path."""


@dataclass(frozen=True)
class Vault:
    """A resolved vault rooted at ``root``.

    Use :func:`discover_vault` to obtain a Vault from a working
    directory. The Vault is immutable; operations that need to mutate
    files take a Vault and modify the filesystem directly.
    """

    root: Path

    @property
    def schema_dir(self) -> Path:
        return self.root / "_Schema"

    @property
    def meta_dir(self) -> Path:
        return self.root / "_Meta"

    @property
    def templates_dir(self) -> Path:
        return self.root / "_Templates"

    @property
    def agents_dir(self) -> Path:
        return self.root / "Agents"

    @property
    def session_log(self) -> Path:
        return self.meta_dir / "Session Log.md"

    @property
    def validator_script(self) -> Path:
        """Path to ``scripts/validate.py`` if present.

        The CLI delegates validation to this script per Roadmap §5
        ("DO NOT REINVENT VALIDATION"). If the script is absent, the
        ``validate`` subcommand reports an actionable error.
        """
        return self.root / "scripts" / "validate.py"

    def folder_for_type(self, note_type: str) -> Path:
        """Return the absolute folder where a note of *note_type* belongs."""
        sub = TYPE_TO_FOLDER.get(note_type)
        if sub is None:
            raise ValueError(f"Unknown note type: {note_type!r}")
        return self.root / sub

    def template_for_type(self, note_type: str) -> Path:
        """Return the absolute path to the template file for *note_type*."""
        name = TYPE_TO_TEMPLATE.get(note_type)
        if name is None:
            raise ValueError(f"No template defined for note type: {note_type!r}")
        return self.templates_dir / name

    def iter_note_files(self) -> Iterable[Path]:
        """Yield every markdown file inside the vault's content folders.

        Used for ID-uniqueness checks. Excludes ``_Templates/`` because
        templates contain placeholder IDs.
        """
        scan = (
            "Concepts", "People", "Organizations", "Papers", "Policies",
            "Debates", "Events", "Datasets", "Cases", "_Synthesis",
            "_Schema", "_Meta", "_Indexes", "Forum", "Agents",
        )
        for sub in scan:
            folder = self.root / sub
            if not folder.exists():
                continue
            for md in folder.rglob("*.md"):
                yield md
        # Top-level markdown files (WHITEPAPER, Home, README)
        for md in self.root.glob("*.md"):
            yield md


def is_vault_root(path: Path) -> bool:
    """Return True if *path* looks like a Nest vault root."""
    if not path.is_dir():
        return False
    if (path / VAULT_MARKER_FILE).exists():
        return True
    return all((path / sub).is_dir() for sub in REQUIRED_SUBDIRS)


def discover_vault(start: Path | None = None, *, max_depth: int = 16) -> Vault:
    """Walk upward from *start* (default: cwd) to find a vault root.

    Raises :class:`VaultNotFoundError` with a helpful message if no
    vault is found within *max_depth* levels.
    """
    current = (start or Path.cwd()).resolve()
    visited: list[Path] = []
    for _ in range(max_depth):
        if is_vault_root(current):
            return Vault(root=current)
        visited.append(current)
        parent = current.parent
        if parent == current:
            break
        current = parent

    paths_tried = "\n  ".join(str(p) for p in visited)
    raise VaultNotFoundError(
        "Could not locate a Nest vault. A vault is a directory containing "
        "_Schema/, _Meta/, and _Templates/ (or a .nest-vault marker file).\n"
        f"Searched upward from:\n  {paths_tried}\n"
        "If you have a vault elsewhere, cd into it and re-run, or pass "
        "--vault-root."
    )


_SLUG_INVALID = re.compile(r"[^a-z0-9\-]+")
_SLUG_MULTIDASH = re.compile(r"-{2,}")


def slugify(text: str) -> str:
    """Convert a free-form title to a kebab-case ASCII slug.

    Implements the slugification rules in ``_Schema/ID Conventions.md``:

    1. Lowercase
    2. Whitespace and underscore become ``-``
    3. Diacritics are stripped (NFD normalize + ascii filter)
    4. Punctuation other than ``-`` is dropped
    5. Multiple ``-`` collapse to one
    6. Leading/trailing ``-`` trimmed
    """
    import unicodedata

    if not text:
        return ""
    # NFD normalize to separate base chars from combining marks, then drop
    # combining marks (this is the standard "ascii-fold" approach).
    normalized = unicodedata.normalize("NFD", text)
    folded = "".join(ch for ch in normalized if not unicodedata.combining(ch))
    s = folded.lower()
    s = s.replace("_", "-")
    s = re.sub(r"\s+", "-", s)
    s = _SLUG_INVALID.sub("-", s)
    s = _SLUG_MULTIDASH.sub("-", s)
    return s.strip("-")


def id_exists_in_vault(vault: Vault, candidate_id: str) -> Path | None:
    """Return the path of the note that already uses *candidate_id*, or None.

    Reads frontmatter ``id:`` lines from every markdown file in the
    vault's content folders. The comparison is exact (kebab-case).
    """
    target_line = f"id: {candidate_id}"
    target_line_quoted = f'id: "{candidate_id}"'
    for md in vault.iter_note_files():
        try:
            text = md.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        if not text.startswith("---"):
            continue
        # Look at just the frontmatter block (between first --- and second ---)
        end = text.find("\n---", 3)
        fm_block = text[:end] if end > 0 else text[:2000]
        for line in fm_block.splitlines():
            stripped = line.strip()
            if stripped == target_line or stripped == target_line_quoted:
                return md
    return None
