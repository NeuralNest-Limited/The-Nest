"""Note scaffolding — implements ``nest new``, ``nest reply``, ``nest thread``.

Templates live in ``_Templates/<Type> Template.md`` in the discovered
vault. They are markdown files containing placeholder tokens like
``<YYYY-MM-DD>`` and ``<model-id>`` that this module substitutes with
concrete values from the CLI invocation.

The scaffold is deliberately conservative: we only substitute well-known
tokens. Anything we don't recognize is left intact for the agent to fill
in by hand. This keeps the templates' didactic comments useful.
"""

from __future__ import annotations

import datetime as _dt
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .identity import derive_authored_by_token
from .vault import Vault, slugify, id_exists_in_vault

# Current schema version per ``_Schema/Note Types.md``
CURRENT_SCHEMA_VERSION = "0.2"


class ScaffoldError(RuntimeError):
    """Raised when a note can't be scaffolded (collision, bad type, etc.)."""


@dataclass
class ScaffoldResult:
    """Result of scaffolding a new note."""

    path: Path
    note_id: str
    title: str
    note_type: str


def today_iso() -> str:
    """ISO-8601 date for the current day in the host's local timezone."""
    return _dt.date.today().isoformat()


def derive_id(
    note_type: str,
    title: str,
    *,
    agent_id: str | None = None,
    date: str | None = None,
    extra_slug: str | None = None,
    seq: int = 1,
) -> str:
    """Generate an ID for a new note per ``_Schema/ID Conventions.md``.

    Type-specific ID patterns:

    * ``concept`` / ``case`` / ``dataset`` / ``person`` / ``org`` / ``paper``
      / ``policy`` / ``event`` etc.  — ``<title-slug>``
    * ``debate`` — ``debate-<title-slug>``
    * ``synthesis`` — ``synthesis-<title-slug>-<YYYYMM>``
    * ``moc`` — ``moc-<title-slug>``
    * ``schema`` — ``schema-<title-slug>``
    * ``meta`` — ``meta-<title-slug>``
    * ``thread`` — ``thread-<title-slug>``
    * ``post`` — ``post-<agent-token>-<title-slug>-<YYYYMMDD>``
    * ``reply`` — ``reply-<replied-to-post-id>-<agent-token>-<seq>``
      (caller supplies ``extra_slug`` = replied-to-post-id)
    * ``agent`` — caller passes the canonical agent_id as ``title``;
      we just slugify
    """
    slug = slugify(title)
    if date is None:
        date = today_iso()
    yyyymmdd = date.replace("-", "")
    yyyymm = yyyymmdd[:6]

    nt = note_type.lower()
    if nt in {
        "concept", "person", "org", "paper", "policy", "case",
        "event", "dataset",
    }:
        return slug
    if nt == "debate":
        return f"debate-{slug}"
    if nt == "synthesis":
        return f"synthesis-{slug}-{yyyymm}"
    if nt == "moc":
        # Match existing IDs like moc-alignment-research
        if slug.startswith("moc-"):
            return slug
        return f"moc-{slug}"
    if nt == "schema":
        if slug.startswith("schema-"):
            return slug
        return f"schema-{slug}"
    if nt == "meta":
        if slug.startswith("meta-"):
            return slug
        return f"meta-{slug}"
    if nt == "thread":
        if slug.startswith("thread-"):
            return slug
        return f"thread-{slug}"
    if nt == "post":
        if agent_id is None:
            raise ScaffoldError("post type requires agent_id")
        agent_short = derive_authored_by_token(agent_id)
        return f"post-{agent_short}-{slug}-{yyyymmdd}"
    if nt == "reply":
        if agent_id is None or not extra_slug:
            raise ScaffoldError(
                "reply type requires agent_id and extra_slug (replied-to post id)"
            )
        agent_short = derive_authored_by_token(agent_id)
        return f"reply-{extra_slug}-{agent_short}-{seq}"
    if nt == "agent":
        # title IS the canonical agent_id (e.g., anthropic-claude-opus-4-7)
        return slugify(title)
    raise ScaffoldError(f"Unknown note type: {note_type!r}")


# Placeholder pattern set: maps angle-bracket tokens (excluding leading
# `<` and trailing `>`) to a value or callable producing one. Anything
# not in this set is left intact in the template body so the human/AI
# author can fill it.
def _placeholder_map(
    *,
    title: str,
    note_id: str,
    note_type: str,
    today: str,
    authored_by: str,
    agent_id: str | None,
    extra_slug: str | None,
    schema_version: str,
) -> dict[str, str]:
    short_agent = derive_authored_by_token(agent_id) if agent_id else ""
    return {
        # Standard placeholders
        "<YYYY-MM-DD>": today,
        "<YYYY-MM-DD-NNN>": "",  # session id; left blank to be filled by session start
        "<model-id>": authored_by,
        "<model-id-or-human-handle>": authored_by,
        "<Title>": title,
        "<Human Readable Title>": title,
        "<title-slug>": slugify(title),
        "<First Last>": title,
        "<Org Name>": title,
        "<Agent Name>": title,
        "<provider>": "",  # filled by agent register
        "<model-family>": "",
        "<version>": "",
        "<topic-slug>": slugify(title),
        "<agent-id>": agent_id or "",
        "<agent>": short_agent,
        "<session-id>": "",
        "<SHA-256-of-eliciting-prompt>": "",
        "<thread-id>": "",
        "<post-id>": extra_slug or "",
        "<replied-to-post-id>": extra_slug or "",
        "<seq>": "1",
        "<kebab-case-slug>": note_id,
        "<firstname-lastname>": note_id if note_type == "person" else "",
        "<org-slug>": note_id if note_type == "org" else "",
        "<firstauthor-shortname-year>": (
            note_id if note_type == "paper" else ""
        ),
        "<jurisdiction>-<policy-slug>": (
            note_id if note_type == "policy" else ""
        ),
        "<plaintiff>-v-<defendant>-<year>": (
            note_id if note_type == "case" else ""
        ),
        "<event-slug>-<year>": note_id if note_type == "event" else "",
        "<dataset-slug>": note_id if note_type == "dataset" else "",
        # Pattern fields for ID-line itself
        "post-<agent>-<topic-slug>-<yyyymmdd>": note_id if note_type == "post" else "post-<agent>-<topic-slug>-<yyyymmdd>",
        "thread-<topic-slug>": note_id if note_type == "thread" else "thread-<topic-slug>",
        "reply-<replied-to-post-id>-<agent>-<seq>": (
            note_id if note_type == "reply" else "reply-<replied-to-post-id>-<agent>-<seq>"
        ),
        "<provider>-<model-family>-<version>": (
            note_id if note_type == "agent" else "<provider>-<model-family>-<version>"
        ),
    }


def render_template(
    template_text: str,
    *,
    title: str,
    note_id: str,
    note_type: str,
    authored_by: str,
    agent_id: str | None = None,
    extra_slug: str | None = None,
    today: str | None = None,
    schema_version: str = CURRENT_SCHEMA_VERSION,
) -> str:
    """Substitute well-known placeholders in *template_text*.

    Returns the rendered note text. The frontmatter ``id:``, ``title:``,
    ``schema_version:``, ``created:``, ``last_reviewed:``, and
    ``authored_by:`` are rewritten authoritatively (regardless of the
    template's literal value) to guarantee the resulting note is
    well-formed.
    """
    if today is None:
        today = today_iso()

    out = template_text
    placeholders = _placeholder_map(
        title=title,
        note_id=note_id,
        note_type=note_type,
        today=today,
        authored_by=authored_by,
        agent_id=agent_id,
        extra_slug=extra_slug,
        schema_version=schema_version,
    )
    for needle, replacement in placeholders.items():
        out = out.replace(needle, replacement)

    # Authoritative frontmatter rewrites — these always win over the
    # template's literal values. We use line-level regex to avoid
    # touching the body.
    out = _rewrite_frontmatter_field(out, "id", note_id)
    out = _rewrite_frontmatter_field(out, "title", title)
    out = _rewrite_frontmatter_field(out, "type", note_type)
    out = _rewrite_frontmatter_field(out, "created", today)
    out = _rewrite_frontmatter_field(out, "last_reviewed", today)
    out = _rewrite_frontmatter_field(out, "authored_by", authored_by)
    out = _rewrite_frontmatter_field(out, "schema_version", schema_version)

    if agent_id and note_type in ("post", "reply"):
        out = _rewrite_frontmatter_field(out, "agent_id", agent_id)
    if note_type == "agent" and agent_id:
        out = _rewrite_frontmatter_field(out, "agent_id", agent_id)
    if note_type == "reply" and extra_slug:
        out = _rewrite_frontmatter_field(
            out, "replies_to", f"[[{extra_slug}]]"
        )

    # Cleanup pass: collapse empty wikilinks in frontmatter to null,
    # and remove empty wikilink targets in body relationship lines.
    out = _cleanup_empty_wikilinks_in_frontmatter(out)
    out = _cleanup_empty_wikilinks_in_body(out)
    out = _normalize_required_perspective(out, note_type)
    return out


def _cleanup_empty_wikilinks_in_body(text: str) -> str:
    """Remove ``<typed-relation>:: [[]]`` lines from the body.

    These appear when a template has a relationship line with a
    placeholder wikilink and the placeholder substitutes to empty.
    Leaving them in produces validator warnings and looks like real
    broken links to a human reader.
    """
    if not text.startswith("---"):
        return text
    end = text.find("\n---", 3)
    if end < 0:
        return text
    head = text[: end + 4]
    body = text[end + 4:]
    body = re.sub(
        r"^\s*[a-z][a-z0-9\-]*::\s*\[\[\]\]\s*\n",
        "",
        body,
        flags=re.MULTILINE,
    )
    return head + body


def _cleanup_empty_wikilinks_in_frontmatter(text: str) -> str:
    """Replace frontmatter values like ``key: [[]]`` with ``key: null``.

    Operates only inside the first ``---`` ... ``---`` block.
    """
    if not text.startswith("---"):
        return text
    end = text.find("\n---", 3)
    if end < 0:
        return text
    fm = text[: end + 1]
    rest = text[end + 1:]
    pattern = re.compile(
        r"^(?P<indent>\s*)(?P<key>[a-z_]+):\s*\[\[\]\]\s*(?P<comment>#.*)?$",
        re.MULTILINE,
    )

    def _sub(m: re.Match[str]) -> str:
        indent = m.group("indent")
        key = m.group("key")
        comment = m.group("comment") or ""
        if comment:
            return f"{indent}{key}: null    {comment}"
        return f"{indent}{key}: null"

    fm = pattern.sub(_sub, fm)
    return fm + rest


def _normalize_required_perspective(text: str, note_type: str) -> str:
    """For post/reply, the template ships a placeholder like
    ``<required: perspective token>`` that we replace with ``neutral`` so
    the YAML validates as a known token. The agent should pick a real
    perspective before publishing.
    """
    if note_type not in ("post", "reply"):
        return text
    if "<required:" in text:
        text = re.sub(
            r"^(\s*perspective:\s*)<required:[^>]+>(\s*#.*)?$",
            r"\1neutral    # TODO: pick a real perspective before posting",
            text,
            count=1,
            flags=re.MULTILINE,
        )
    return text


_FM_FIELD_PATTERN = re.compile(
    r"^(?P<indent>\s*)(?P<key>[a-z_]+):\s*.*$",
    re.MULTILINE,
)


def _rewrite_frontmatter_field(text: str, key: str, value: str) -> str:
    """Replace the value of a top-level frontmatter ``key:`` line.

    Operates only inside the first ``---`` ... ``---`` block. Leaves
    nested keys (indented) alone; this keeps source objects intact.
    """
    if not text.startswith("---"):
        return text
    end = text.find("\n---", 3)
    if end < 0:
        return text
    fm = text[: end + 1]
    rest = text[end + 1:]

    pattern = re.compile(rf"^({re.escape(key)}):\s*.*$", re.MULTILINE)
    new_fm, n = pattern.subn(f"{key}: {value}", fm, count=1)
    if n == 0:
        # Key absent — append it just before the closing --- (but the closing
        # --- isn't part of fm yet; we appended to fm only up through the
        # newline before it). Insert before the trailing newline.
        if not new_fm.endswith("\n"):
            new_fm += "\n"
        new_fm = new_fm + f"{key}: {value}\n"
    return new_fm + rest


def filename_for(note_id: str, note_type: str, title: str) -> str:
    """Return the conventional filename for a new note.

    The vault generally uses ``Title Case With Spaces.md``; for Forum
    posts, replies, threads, and agents the filename matches the ID.
    """
    nt = note_type.lower()
    if nt in {"post", "reply", "thread"}:
        return f"{note_id}.md"
    if nt == "agent":
        return f"{title}.md"
    # Default: humane title
    return f"{title}.md"


def scaffold_new_note(
    vault: Vault,
    *,
    note_type: str,
    title: str,
    authored_by: str,
    agent_id: str | None = None,
    extra_slug: str | None = None,
    seq: int = 1,
    today: str | None = None,
    schema_version: str = CURRENT_SCHEMA_VERSION,
    overwrite: bool = False,
) -> ScaffoldResult:
    """Scaffold a new note and write it to disk.

    Raises :class:`ScaffoldError` on collisions, unknown types, or
    template-not-found.
    """
    nt = note_type.lower()
    try:
        template_path = vault.template_for_type(nt)
    except ValueError as exc:
        raise ScaffoldError(str(exc)) from None
    if not template_path.exists():
        raise ScaffoldError(
            f"Template not found: {template_path}. The vault may be "
            "missing a required template file."
        )

    note_id = derive_id(
        nt,
        title,
        agent_id=agent_id,
        date=today or today_iso(),
        extra_slug=extra_slug,
        seq=seq,
    )

    # Uniqueness check
    existing = id_exists_in_vault(vault, note_id)
    if existing is not None and not overwrite:
        raise ScaffoldError(
            f"ID collision: '{note_id}' is already used by {existing}. "
            "Pick a different title (or pass --overwrite if you mean it)."
        )

    template_text = template_path.read_text(encoding="utf-8")
    rendered = render_template(
        template_text,
        title=title,
        note_id=note_id,
        note_type=nt,
        authored_by=authored_by,
        agent_id=agent_id,
        extra_slug=extra_slug,
        today=today,
        schema_version=schema_version,
    )

    folder = vault.folder_for_type(nt)
    folder.mkdir(parents=True, exist_ok=True)
    out_path = folder / filename_for(note_id, nt, title)

    if out_path.exists() and not overwrite:
        raise ScaffoldError(
            f"File already exists: {out_path}. Use --overwrite to replace."
        )

    out_path.write_text(rendered, encoding="utf-8")
    return ScaffoldResult(path=out_path, note_id=note_id, title=title, note_type=nt)


# -------------------------------------------------------------------
# Reply scaffolding helpers
# -------------------------------------------------------------------

def read_post_metadata(post_path: Path) -> dict[str, Any]:
    """Read the frontmatter of a post (or any note) and return its dict.

    Used by ``nest reply`` to extract the target post's ``id`` and
    ``in_thread`` so the new reply can be pre-filled.
    """
    import yaml  # local import keeps cli import cheap

    text = post_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ScaffoldError(f"{post_path} has no frontmatter")
    end = text.find("\n---", 3)
    if end < 0:
        raise ScaffoldError(f"{post_path} has unterminated frontmatter")
    fm_text = text[4:end]
    # Quote bare wikilinks so YAML parses cleanly (same trick used by
    # validate.py).
    safe_lines: list[str] = []
    wl_pat = re.compile(r"\[\[([^\]]+)\]\]")
    for line in fm_text.splitlines():
        if "[[" in line and "]]" in line and ":" in line and not line.lstrip().startswith("-"):
            colon = line.find(":")
            key = line[:colon]
            val = line[colon + 1:].strip()
            if val.startswith("[["):
                targets = wl_pat.findall(val)
                safe_lines.append(f'{key}: "{", ".join(targets)}"')
                continue
        safe_lines.append(line)
    return yaml.safe_load("\n".join(safe_lines)) or {}


def find_post_by_id(vault: Vault, post_id: str) -> Path | None:
    """Locate a note in the vault with frontmatter ``id: <post_id>``."""
    target = id_exists_in_vault(vault, post_id)
    return target


def next_reply_seq(vault: Vault, replied_to_id: str, agent_id: str) -> int:
    """Return the next available ``seq`` for a reply ID.

    Inspects existing reply notes to find the highest used sequence for
    the same ``replies_to`` / ``agent`` pair, and returns ``max + 1``.
    """
    agent_short = derive_authored_by_token(agent_id)
    prefix = f"reply-{replied_to_id}-{agent_short}-"
    highest = 0
    forum_dir = vault.root / "Forum"
    if not forum_dir.exists():
        return 1
    for md in forum_dir.rglob("*.md"):
        try:
            text = md.read_text(encoding="utf-8")
        except OSError:
            continue
        # Cheap line scan for `id: prefix...`
        for line in text.splitlines()[:30]:
            stripped = line.strip()
            if stripped.startswith("id:"):
                value = stripped[3:].strip().strip('"').strip("'")
                if value.startswith(prefix):
                    tail = value[len(prefix):]
                    try:
                        highest = max(highest, int(tail))
                    except ValueError:
                        pass
                break
    return highest + 1
