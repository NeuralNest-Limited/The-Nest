"""Tests for the git/commit subsystem."""

from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

from nest_cli.commit import (
    GitError, build_commit_message, collect_session_commits,
    current_branch, is_git_repo, stage_and_commit,
)


# ----- build_commit_message -----------------------------------------

def test_build_commit_message_with_scope() -> None:
    msg = build_commit_message(
        commit_type="note",
        scope="concepts",
        subject="add mesa-optimization",
        session_id="2026-05-20-001",
        author_agent="claude-opus-4-7",
    )
    assert msg.startswith("note(concepts): add mesa-optimization")
    assert "Session: 2026-05-20-001" in msg
    assert "Author-agent: claude-opus-4-7" in msg


def test_build_commit_message_without_scope() -> None:
    msg = build_commit_message(
        commit_type="chore",
        scope=None,
        subject="bump version",
    )
    assert msg.startswith("chore: bump version")


def test_build_commit_message_with_body() -> None:
    msg = build_commit_message(
        commit_type="fix",
        scope="papers",
        subject="correct year",
        body="Source verification flagged conflict.",
        session_id="x",
    )
    assert "Source verification" in msg
    # Blank line before body and before trailers
    lines = msg.split("\n")
    assert "" in lines  # at least one blank-line separator


def test_build_commit_message_requires_subject() -> None:
    with pytest.raises(ValueError):
        build_commit_message(commit_type="fix", scope="x", subject="")


def test_build_commit_message_requires_type() -> None:
    with pytest.raises(ValueError):
        build_commit_message(commit_type="", scope="x", subject="y")


# ----- git operations against temp_git_vault ------------------------

def test_is_git_repo_true(temp_git_vault: Path) -> None:
    assert is_git_repo(temp_git_vault)


def test_is_git_repo_false(temp_vault: Path) -> None:
    assert not is_git_repo(temp_vault)


def test_current_branch_returns_main(temp_git_vault: Path) -> None:
    assert current_branch(temp_git_vault) == "main"


def test_stage_and_commit_succeeds(temp_git_vault: Path) -> None:
    new_file = temp_git_vault / "Concepts" / "Test.md"
    new_file.write_text(
        "---\nid: t\ntitle: t\ntype: concept\nstatus: stub\n"
        "created: 2026-05-20\nlast_reviewed: 2026-05-20\n"
        "authored_by: x\nschema_version: 0.2\n---\n",
        encoding="utf-8",
    )
    result = stage_and_commit(
        temp_git_vault,
        [new_file],
        commit_type="note",
        scope="concepts",
        subject="add test stub",
        session_id="2026-05-20-099",
        author_agent="claude-opus-4-7",
    )
    assert len(result.sha) >= 7
    # Verify the commit message has the trailers
    out = subprocess.run(
        ["git", "log", "-1", "--pretty=%B"],
        cwd=temp_git_vault, capture_output=True, text=True, check=True,
    )
    assert "Session: 2026-05-20-099" in out.stdout
    assert "Author-agent: claude-opus-4-7" in out.stdout


def test_stage_and_commit_empty_files_raises(temp_git_vault: Path) -> None:
    with pytest.raises(GitError):
        stage_and_commit(
            temp_git_vault, [],
            commit_type="x", scope="y", subject="z",
        )


def test_collect_session_commits_returns_matching(temp_git_vault: Path) -> None:
    nf = temp_git_vault / "Concepts" / "A.md"
    nf.write_text(
        "---\nid: a\ntitle: a\ntype: concept\nstatus: stub\n"
        "created: 2026-05-20\nlast_reviewed: 2026-05-20\n"
        "authored_by: x\nschema_version: 0.2\n---\n",
        encoding="utf-8",
    )
    stage_and_commit(
        temp_git_vault, [nf],
        commit_type="note", scope="concepts", subject="add a",
        session_id="2026-05-20-100", author_agent="x",
    )
    shas = collect_session_commits(temp_git_vault, "2026-05-20-100")
    assert len(shas) == 1


def test_collect_session_commits_empty_for_unknown(temp_git_vault: Path) -> None:
    shas = collect_session_commits(temp_git_vault, "9999-99-99-999")
    assert shas == []
