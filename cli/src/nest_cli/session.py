"""Session Log manipulation — ``nest session start``, ``nest session end``.

The Session Log lives at ``_Meta/Session Log.md``. Each session is a
top-of-list YAML block followed by a ``## Body — <id>`` section. The
CLI's session commands insert and finalize entries.

The Roadmap §5 mandates: *"READ the file before EDIT (recurring pitfall
mentioned in prior session logs)."* This module always reads the
existing log before mutating it.
"""

from __future__ import annotations

import datetime as _dt
import os
import re
from dataclasses import dataclass
from pathlib import Path

from .vault import Vault


ENV_VAR = "NEST_SESSION_ID"
SESSION_HEADER_RE = re.compile(r"^## (?P<id>\d{4}-\d{2}-\d{2}-\d{3})\s*$", re.MULTILINE)


@dataclass
class SessionEntry:
    """In-memory representation of a Session Log entry."""

    session_id: str
    agent: str
    focus: str
    started_iso: str
    ended_iso: str | None = None
    commits: list[str] | None = None
    next_session_seed: str | None = None
    human_collaborator: str | None = None


class SessionLogError(RuntimeError):
    """Raised on session log parse / mutation errors."""


def now_iso() -> str:
    """Return the current local datetime in ISO-8601 with timezone."""
    return _dt.datetime.now().astimezone().isoformat(timespec="seconds")


def today_str() -> str:
    return _dt.date.today().isoformat()


def next_session_id(log_text: str, *, date: str | None = None) -> str:
    """Compute the next session_id (``YYYY-MM-DD-NNN``) for *date*.

    Scans *log_text* for existing IDs matching the date prefix; returns
    ``<date>-<max+1>`` (zero-padded to 3 digits). If *date* is None,
    uses today.
    """
    if date is None:
        date = today_str()
    existing: list[int] = []
    for m in SESSION_HEADER_RE.finditer(log_text):
        sid = m.group("id")
        if sid.startswith(date + "-"):
            try:
                existing.append(int(sid.rsplit("-", 1)[1]))
            except ValueError:
                continue
    nxt = max(existing) + 1 if existing else 1
    return f"{date}-{nxt:03d}"


def build_session_open_block(entry: SessionEntry) -> str:
    """Render a session entry as the open-state YAML+body block.

    The block matches the template at the top of ``_Meta/Session Log.md``
    and is intended to be inserted directly above the previous entry.
    """
    yaml_lines = [
        f"session_id: {entry.session_id}",
        f"agent: {entry.agent}",
    ]
    if entry.human_collaborator:
        yaml_lines.append(f"human_collaborator: {entry.human_collaborator}")
    yaml_lines.extend([
        f"started: {entry.started_iso}",
        "ended: <pending>",
        f"focus: {entry.focus}",
        "commits: <pending>",
        "notes_created: []",
        "notes_modified: []",
        "backlog_items_completed: []",
        "backlog_items_added: []",
        "open_issues: []",
        "escalations: []",
        "next_session_seed: <pending>",
    ])
    yaml_block = "\n".join(yaml_lines)
    return (
        f"## {entry.session_id}\n\n"
        f"```yaml\n{yaml_block}\n```\n\n"
        f"## Body — {entry.session_id}\n\n"
        "Session opened via `nest session start`. Fill in narrative as work proceeds.\n\n"
        "---\n\n"
    )


# Marker that indicates where new entries should be inserted: the line
# `---` immediately after the template section, just before the first
# `## YYYY-MM-DD-NNN` heading.
ENTRY_INSERT_MARKER = "Then a `## Body — <session_id>` section with prose context."


def insert_session_entry(log_text: str, entry_block: str) -> str:
    """Insert *entry_block* at the top of the entries list.

    Strategy: find the first ``## <session_id>`` heading and insert
    immediately before it. If no entries exist yet, insert after the
    template-section divider.
    """
    m = SESSION_HEADER_RE.search(log_text)
    if m:
        idx = m.start()
        return log_text[:idx] + entry_block + log_text[idx:]
    # No prior entries: append at the very end after a blank line.
    if not log_text.endswith("\n"):
        log_text += "\n"
    return log_text + "\n" + entry_block


def start_session(
    vault: Vault,
    *,
    agent_id: str,
    focus: str,
    human_collaborator: str | None = None,
    write_env_hint: bool = True,
) -> SessionEntry:
    """Open a new session: insert entry at top of Session Log.

    Returns the constructed :class:`SessionEntry` (with the freshly
    minted session_id). Does **not** export ``NEST_SESSION_ID`` into the
    caller's environment (a subprocess can't do that for the parent).
    Instead, the calling CLI prints an instruction line that the user
    can ``eval``.
    """
    log_path = vault.session_log
    if not log_path.exists():
        raise SessionLogError(
            f"Session log not found at {log_path}. Has the vault been "
            "fully initialized?"
        )
    log_text = log_path.read_text(encoding="utf-8")
    sid = next_session_id(log_text)
    entry = SessionEntry(
        session_id=sid,
        agent=agent_id,
        focus=focus or "<not specified>",
        started_iso=now_iso(),
        human_collaborator=human_collaborator,
    )
    block = build_session_open_block(entry)
    new_log = insert_session_entry(log_text, block)
    log_path.write_text(new_log, encoding="utf-8")
    return entry


def end_session(
    vault: Vault,
    *,
    session_id: str,
    summary: str | None = None,
    commits: list[str] | None = None,
    next_session_seed: str | None = None,
) -> SessionEntry:
    """Close an open session entry: fill ``ended:`` and ``commits:``.

    Operates by reading the file, locating the YAML block for the
    matching ``## <session_id>`` heading, and rewriting the
    ``ended:``, ``commits:``, ``next_session_seed:`` lines.
    """
    log_path = vault.session_log
    if not log_path.exists():
        raise SessionLogError(f"Session log not found at {log_path}.")
    log_text = log_path.read_text(encoding="utf-8")

    # Find the entry's YAML block
    header_re = re.compile(rf"^## {re.escape(session_id)}\s*$", re.MULTILINE)
    m = header_re.search(log_text)
    if not m:
        raise SessionLogError(
            f"Session {session_id} not found in {log_path}."
        )

    # Find the ```yaml ... ``` block following the heading
    after = log_text[m.end():]
    yaml_open = after.find("```yaml")
    if yaml_open < 0:
        raise SessionLogError(
            f"Session {session_id} has no YAML block."
        )
    yaml_end = after.find("```", yaml_open + len("```yaml"))
    if yaml_end < 0:
        raise SessionLogError(
            f"Session {session_id} YAML block not terminated."
        )

    yaml_block = after[yaml_open + len("```yaml"):yaml_end]
    new_yaml = yaml_block

    # Update fields
    new_yaml = _replace_yaml_field(new_yaml, "ended", now_iso())
    if commits is not None:
        if commits:
            commit_lines = "\n".join(f"  - {sha}" for sha in commits)
            new_yaml = _replace_yaml_field_block(
                new_yaml, "commits", commit_lines
            )
        else:
            new_yaml = _replace_yaml_field(new_yaml, "commits", "[]")

    if next_session_seed is not None and next_session_seed.strip():
        # Render multi-line value with literal block scalar
        seed_block = "\n".join(
            f"  {line}" for line in next_session_seed.strip().splitlines()
        )
        new_yaml = _replace_yaml_field_block(
            new_yaml, "next_session_seed", "|\n" + seed_block
        )

    # Reconstruct full log
    new_after = (
        after[:yaml_open + len("```yaml")]
        + new_yaml
        + after[yaml_end:]
    )
    new_log = log_text[:m.end()] + new_after

    # Optional: append summary to body
    if summary:
        # Find the `## Body — <id>` section and append a closing paragraph
        body_re = re.compile(
            rf"^## Body — {re.escape(session_id)}\s*$", re.MULTILINE
        )
        bm = body_re.search(new_log)
        if bm:
            # Find end of section: next `## ` or `---` or EOF
            tail_start = bm.end()
            next_section = re.search(
                r"^(## |---\s*$)", new_log[tail_start:], re.MULTILINE
            )
            insertion_point = (
                tail_start + next_section.start() if next_section else len(new_log)
            )
            paragraph = f"\n\n**Closing summary**: {summary.strip()}\n"
            new_log = (
                new_log[:insertion_point].rstrip()
                + paragraph
                + ("\n" + new_log[insertion_point:] if next_section else "")
            )

    log_path.write_text(new_log, encoding="utf-8")

    return SessionEntry(
        session_id=session_id,
        agent="",  # not modified
        focus="",
        started_iso="",
        ended_iso=now_iso(),
        commits=commits or [],
        next_session_seed=next_session_seed,
    )


def _replace_yaml_field(yaml_text: str, key: str, value: str) -> str:
    """Replace a top-level scalar field in a YAML text block."""
    pattern = re.compile(
        rf"^(?P<indent>\s*){re.escape(key)}:.*$", re.MULTILINE
    )
    if pattern.search(yaml_text):
        return pattern.sub(f"{key}: {value}", yaml_text, count=1)
    # Append before closing
    if not yaml_text.endswith("\n"):
        yaml_text += "\n"
    return yaml_text + f"{key}: {value}\n"


def _replace_yaml_field_block(yaml_text: str, key: str, replacement: str) -> str:
    """Replace a top-level YAML key whose value may span multiple lines.

    Locates the line ``<key>: ...`` and any indented continuation lines,
    then substitutes the entire block with ``<key>: <replacement>``.
    """
    lines = yaml_text.split("\n")
    out: list[str] = []
    i = 0
    found = False
    while i < len(lines):
        line = lines[i]
        m = re.match(rf"^(?P<indent>\s*){re.escape(key)}:(?P<rest>.*)$", line)
        if m and not found:
            indent = m.group("indent")
            found = True
            # Render replacement block
            if "\n" in replacement:
                head, _, tail = replacement.partition("\n")
                out.append(f"{indent}{key}: {head}")
                for r in tail.split("\n"):
                    out.append(r)
            else:
                out.append(f"{indent}{key}: {replacement}")
            # Skip continuation lines (indented more than `indent`)
            i += 1
            while i < len(lines):
                nxt = lines[i]
                if nxt.strip() == "":
                    # blank line ends the value only if next line is dedented
                    if i + 1 < len(lines) and (
                        len(lines[i + 1]) - len(lines[i + 1].lstrip()) <= len(indent)
                    ):
                        break
                    out.append(nxt)
                    i += 1
                    continue
                nxt_indent = len(nxt) - len(nxt.lstrip())
                if nxt_indent > len(indent):
                    i += 1
                    continue
                break
            continue
        out.append(line)
        i += 1
    if not found:
        # Field absent — append
        if not out or out[-1] != "":
            out.append("")
        if "\n" in replacement:
            head, _, tail = replacement.partition("\n")
            out.append(f"{key}: {head}")
            for r in tail.split("\n"):
                out.append(r)
        else:
            out.append(f"{key}: {replacement}")
    return "\n".join(out)


def current_session_id() -> str | None:
    """Return the value of ``$NEST_SESSION_ID`` or None if unset."""
    return os.environ.get(ENV_VAR) or None
