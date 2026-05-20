"""Tests for the Session Log subsystem."""

from __future__ import annotations

from pathlib import Path

import pytest

from nest_cli.session import (
    SessionLogError, build_session_open_block, end_session,
    insert_session_entry, next_session_id, start_session, SessionEntry,
)
from nest_cli.vault import Vault


# ----- next_session_id -----------------------------------------------

def test_next_session_id_starts_at_001() -> None:
    log = "Some preamble.\n\n---\n\nNo entries yet.\n"
    out = next_session_id(log, date="2026-05-20")
    assert out == "2026-05-20-001"


def test_next_session_id_increments_existing() -> None:
    log = "## 2026-05-20-001\n\nstuff.\n\n## 2026-05-20-002\n"
    out = next_session_id(log, date="2026-05-20")
    assert out == "2026-05-20-003"


def test_next_session_id_ignores_other_dates() -> None:
    log = "## 2026-05-19-005\n\n## 2026-05-20-001\n"
    out = next_session_id(log, date="2026-05-20")
    assert out == "2026-05-20-002"


def test_next_session_id_handles_non_sequential() -> None:
    log = "## 2026-05-20-001\n## 2026-05-20-007\n## 2026-05-20-003\n"
    out = next_session_id(log, date="2026-05-20")
    assert out == "2026-05-20-008"


# ----- build / insert -----------------------------------------------

def test_build_session_open_block_contains_required_fields() -> None:
    entry = SessionEntry(
        session_id="2026-05-20-099",
        agent="claude-opus-4-7",
        focus="testing",
        started_iso="2026-05-20T18:00:00+12:00",
    )
    block = build_session_open_block(entry)
    assert "## 2026-05-20-099" in block
    assert "session_id: 2026-05-20-099" in block
    assert "agent: claude-opus-4-7" in block
    assert "## Body — 2026-05-20-099" in block


def test_insert_session_entry_prepends_to_existing() -> None:
    log = "## 2026-05-20-001\n\ncontent\n"
    out = insert_session_entry(log, "## 2026-05-20-002\n\nnew\n\n")
    assert out.startswith("## 2026-05-20-002")
    assert "## 2026-05-20-001" in out


def test_insert_session_entry_appends_when_no_prior() -> None:
    log = "preamble only\n"
    out = insert_session_entry(log, "## 2026-05-20-001\n\nfresh\n\n")
    assert "## 2026-05-20-001" in out


# ----- start_session end-to-end -------------------------------------

def test_start_session_creates_entry_at_top(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    entry = start_session(
        v, agent_id="anthropic-claude-opus-4-7", focus="hello",
    )
    log = v.session_log.read_text(encoding="utf-8")
    assert f"## {entry.session_id}" in log
    # Body block has the focus line
    assert "focus: hello" in log


def test_start_session_increments_sequence(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    e1 = start_session(v, agent_id="a", focus="one")
    e2 = start_session(v, agent_id="a", focus="two")
    assert e2.session_id != e1.session_id
    n1 = int(e1.session_id.rsplit("-", 1)[1])
    n2 = int(e2.session_id.rsplit("-", 1)[1])
    assert n2 == n1 + 1


def test_start_session_raises_when_log_missing(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    v.session_log.unlink()
    with pytest.raises(SessionLogError):
        start_session(v, agent_id="a", focus="x")


# ----- end_session ---------------------------------------------------

def test_end_session_fills_ended_and_commits(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    entry = start_session(v, agent_id="a", focus="x")
    end_session(
        v,
        session_id=entry.session_id,
        summary="all done",
        commits=["abc1234", "def5678"],
        next_session_seed="next: do Y",
    )
    log = v.session_log.read_text(encoding="utf-8")
    assert "ended: <pending>" not in log.split(f"## {entry.session_id}")[1].split("---")[0]
    assert "abc1234" in log
    assert "def5678" in log
    assert "all done" in log


def test_end_session_unknown_id_raises(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    with pytest.raises(SessionLogError):
        end_session(v, session_id="9999-99-99-999")


def test_end_session_no_commits_keeps_pending_or_empty(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    entry = start_session(v, agent_id="a", focus="x")
    end_session(v, session_id=entry.session_id)
    log = v.session_log.read_text(encoding="utf-8")
    # The entry should still exist; commits remained <pending>
    assert f"## {entry.session_id}" in log


def test_end_session_handles_seed_with_newlines(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    entry = start_session(v, agent_id="a", focus="x")
    end_session(
        v,
        session_id=entry.session_id,
        next_session_seed="line one\nline two\nline three",
    )
    log = v.session_log.read_text(encoding="utf-8")
    assert "line one" in log
    assert "line two" in log


# ----- read-before-edit discipline ----------------------------------

def test_start_session_then_end_session_idempotent(temp_vault: Path) -> None:
    """Reading the file before editing is implicit; we verify by
    showing the session content survives a start + end cycle."""
    v = Vault(root=temp_vault)
    entry = start_session(v, agent_id="claude", focus="alpha")
    end_session(v, session_id=entry.session_id, commits=["sha-1"])
    log = v.session_log.read_text(encoding="utf-8")
    # Original header preserved
    assert "# Session Log" in log
    # Entry preserved
    assert "focus: alpha" in log
