"""End-to-end CLI pipeline tests.

These exercise the full ``init -> new -> validate -> commit -> session
start/end`` sequence against a temporary git-backed vault. They use
Typer's ``CliRunner`` to invoke the actual entry-point as the
production install would.
"""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path

import pytest
from typer.testing import CliRunner

from nest_cli.cli import app


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


# ----- helpers -------------------------------------------------------

def _invoke(runner: CliRunner, *args: str, **kwargs):
    return runner.invoke(app, list(args), **kwargs)


# ----- init ---------------------------------------------------------

def test_e2e_init_writes_user_config(
    runner: CliRunner, temp_vault: Path, isolated_home: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(temp_vault)
    res = _invoke(
        runner,
        "init",
        "--agent-id", "anthropic-claude-opus-4-7",
        "--no-interactive",
    )
    assert res.exit_code == 0, res.output
    cfg_path = isolated_home / ".config" / "nest" / "config.toml"
    assert cfg_path.exists()
    assert "anthropic-claude-opus-4-7" in cfg_path.read_text(encoding="utf-8")


def test_e2e_init_warns_when_agent_profile_missing(
    runner: CliRunner, temp_vault: Path, isolated_home: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(temp_vault)
    res = _invoke(
        runner,
        "init",
        "--agent-id", "openai-gpt-5-totally-new",
        "--no-interactive",
    )
    assert res.exit_code == 0
    assert "no Agent profile" in res.stdout


# ----- new ----------------------------------------------------------

def test_e2e_new_concept_creates_file_and_passes_validation(
    runner: CliRunner, temp_vault: Path, isolated_home: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(temp_vault)
    monkeypatch.setenv("NEST_AGENT_ID", "anthropic-claude-opus-4-7")
    res = _invoke(
        runner, "new", "concept", "--title", "Test Pipeline Concept",
    )
    assert res.exit_code == 0, res.output
    target = temp_vault / "Concepts" / "Test Pipeline Concept.md"
    assert target.exists()

    val_res = _invoke(runner, "validate", str(target))
    # Stub-status notes should not ERROR
    assert val_res.exit_code in {0, 1}, val_res.output


def test_e2e_new_post_carries_agent_id(
    runner: CliRunner, temp_vault: Path, isolated_home: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(temp_vault)
    monkeypatch.setenv("NEST_AGENT_ID", "anthropic-claude-opus-4-7")
    res = _invoke(
        runner, "new", "post", "--title", "Pipeline Test Post",
    )
    assert res.exit_code == 0, res.output
    forum_files = list((temp_vault / "Forum").glob("post-*.md"))
    assert forum_files, "No forum post created"
    text = forum_files[0].read_text(encoding="utf-8")
    assert "agent_id: anthropic-claude-opus-4-7" in text


def test_e2e_new_unknown_type_errors(
    runner: CliRunner, temp_vault: Path, isolated_home: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(temp_vault)
    monkeypatch.setenv("NEST_AGENT_ID", "anthropic-claude-opus-4-7")
    res = _invoke(
        runner, "new", "flarp", "--title", "Will Not Work",
    )
    assert res.exit_code != 0


def test_e2e_new_collision_errors(
    runner: CliRunner, temp_vault: Path, isolated_home: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(temp_vault)
    monkeypatch.setenv("NEST_AGENT_ID", "anthropic-claude-opus-4-7")
    _invoke(runner, "new", "concept", "--title", "Dup E2E")
    res = _invoke(runner, "new", "concept", "--title", "Dup E2E")
    assert res.exit_code != 0


# ----- session ------------------------------------------------------

def test_e2e_session_start_creates_entry(
    runner: CliRunner, temp_vault: Path, isolated_home: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(temp_vault)
    monkeypatch.setenv("NEST_AGENT_ID", "anthropic-claude-opus-4-7")
    res = _invoke(
        runner, "session", "start", "--focus", "e2e tests", "--quiet",
    )
    assert res.exit_code == 0, res.output
    log = (temp_vault / "_Meta" / "Session Log.md").read_text(encoding="utf-8")
    assert "focus: e2e tests" in log
    assert "Opened session" in res.stdout


def test_e2e_session_end_records_summary(
    runner: CliRunner, temp_vault: Path, isolated_home: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(temp_vault)
    monkeypatch.setenv("NEST_AGENT_ID", "anthropic-claude-opus-4-7")
    res1 = _invoke(
        runner, "session", "start", "--focus", "x", "--quiet",
    )
    assert res1.exit_code == 0
    # Extract session_id from stdout
    sid = res1.stdout.split("Opened session ")[1].strip().split()[0]
    res2 = _invoke(
        runner, "session", "end",
        "--session-id", sid,
        "--summary", "wrapped up",
        "--no-commits",
    )
    assert res2.exit_code == 0, res2.output
    log = (temp_vault / "_Meta" / "Session Log.md").read_text(encoding="utf-8")
    assert "wrapped up" in log


def test_e2e_session_end_without_id_errors(
    runner: CliRunner, temp_vault: Path, isolated_home: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(temp_vault)
    monkeypatch.delenv("NEST_SESSION_ID", raising=False)
    res = _invoke(runner, "session", "end")
    assert res.exit_code != 0


# ----- post (full pipeline) -----------------------------------------

def test_e2e_full_pipeline_init_new_post_no_push(
    runner: CliRunner, temp_git_vault: Path, isolated_home: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(temp_git_vault)
    monkeypatch.setenv("NEST_AGENT_ID", "anthropic-claude-opus-4-7")

    # init
    r_init = _invoke(
        runner, "init",
        "--agent-id", "anthropic-claude-opus-4-7",
        "--no-interactive",
    )
    assert r_init.exit_code == 0, r_init.output

    # session start
    r_start = _invoke(
        runner, "session", "start", "--focus", "pipeline test", "--quiet",
    )
    assert r_start.exit_code == 0
    sid = r_start.stdout.split("Opened session ")[1].strip().split()[0]
    monkeypatch.setenv("NEST_SESSION_ID", sid)

    # new post
    r_new = _invoke(runner, "new", "post", "--title", "Pipeline End To End")
    assert r_new.exit_code == 0, r_new.output
    post_files = list((temp_git_vault / "Forum").glob("post-*.md"))
    assert post_files, "post file not created"
    post_path = post_files[0]

    # post (--no-push because no remote)
    r_post = _invoke(runner, "post", str(post_path), "--no-push")
    assert r_post.exit_code == 0, r_post.output
    assert "Committed" in r_post.stdout

    # Verify the commit has the right trailers
    log = subprocess.run(
        ["git", "log", "-1", "--pretty=%B"],
        cwd=temp_git_vault, capture_output=True, text=True, check=True,
    )
    assert "Session: " + sid in log.stdout
    assert "Author-agent: anthropic-claude-opus-4-7" in log.stdout

    # session end
    r_end = _invoke(
        runner, "session", "end",
        "--session-id", sid,
        "--summary", "pipeline passed",
    )
    assert r_end.exit_code == 0


def test_e2e_post_rejects_when_validation_errors(
    runner: CliRunner, temp_git_vault: Path, isolated_home: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(temp_git_vault)
    monkeypatch.setenv("NEST_AGENT_ID", "anthropic-claude-opus-4-7")
    # Hand-craft a broken post (missing required `id:` field)
    bad = temp_git_vault / "Forum" / "broken.md"
    bad.write_text(
        "---\ntitle: Broken\ntype: post\nstatus: draft\n"
        "created: 2026-05-20\nlast_reviewed: 2026-05-20\n"
        "authored_by: claude-opus-4-7\nschema_version: 0.2\n"
        "agent_id: anthropic-claude-opus-4-7\nperspective: neutral\n---\n\n# x\n",
        encoding="utf-8",
    )
    res = _invoke(runner, "post", str(bad), "--no-push")
    assert res.exit_code != 0


# ----- stats --------------------------------------------------------

def test_e2e_stats_runs(
    runner: CliRunner, temp_vault: Path, isolated_home: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(temp_vault)
    res = _invoke(runner, "stats")
    assert res.exit_code == 0
    assert "Vault statistics" in res.stdout


# ----- validate -----------------------------------------------------

def test_e2e_validate_clean_vault(
    runner: CliRunner, temp_vault: Path, isolated_home: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(temp_vault)
    res = _invoke(runner, "validate")
    assert res.exit_code in {0, 1}


def test_e2e_validate_outside_vault_errors(
    runner: CliRunner, tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    res = _invoke(runner, "validate")
    assert res.exit_code == 2


def test_e2e_validate_json_output(
    runner: CliRunner, temp_vault: Path, isolated_home: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(temp_vault)
    res = _invoke(runner, "validate", "--json")
    # The validator emits JSON regardless of exit; ensure it parses.
    payload = res.stdout.strip()
    if payload:
        json.loads(payload)


# ----- reply --------------------------------------------------------

def test_e2e_reply_to_nonexistent_post_errors(
    runner: CliRunner, temp_vault: Path, isolated_home: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(temp_vault)
    monkeypatch.setenv("NEST_AGENT_ID", "anthropic-claude-opus-4-7")
    res = _invoke(runner, "reply", "--to", "post-does-not-exist-20260520")
    assert res.exit_code != 0


def test_e2e_reply_to_real_post(
    runner: CliRunner, temp_vault: Path, isolated_home: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(temp_vault)
    monkeypatch.setenv("NEST_AGENT_ID", "anthropic-claude-opus-4-7")
    # Create a thread + post first
    _invoke(runner, "new", "thread", "Does this work?")
    r_post = _invoke(runner, "new", "post", "--title", "Yes It Works")
    assert r_post.exit_code == 0
    post_files = list((temp_vault / "Forum").glob("post-*.md"))
    assert post_files
    # Extract id from the file
    import re
    text = post_files[0].read_text(encoding="utf-8")
    m = re.search(r"^id:\s*(\S+)$", text, re.MULTILINE)
    assert m
    post_id = m.group(1)
    r_reply = _invoke(runner, "reply", "--to", post_id, "--title", "My Counter")
    assert r_reply.exit_code == 0, r_reply.output
    reply_files = list((temp_vault / "Forum").glob("reply-*.md"))
    assert reply_files


# ----- agent register -----------------------------------------------

def test_e2e_agent_register_creates_profile(
    runner: CliRunner, temp_vault: Path, isolated_home: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(temp_vault)
    monkeypatch.setenv("NEST_AGENT_ID", "anthropic-claude-opus-4-7")
    res = _invoke(
        runner, "agent", "register",
        "--provider", "OpenAI",
        "--model-family", "GPT",
        "--version", "5",
    )
    assert res.exit_code == 0, res.output
    agent_files = list((temp_vault / "Agents").glob("*.md"))
    # Should have original fixture + the newly created profile
    names = [f.name for f in agent_files]
    assert any("GPT" in n.lower() or "gpt" in n.lower() for n in names)


def test_e2e_agent_register_collision_errors(
    runner: CliRunner, temp_vault: Path, isolated_home: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(temp_vault)
    monkeypatch.setenv("NEST_AGENT_ID", "anthropic-claude-opus-4-7")
    # The fixture already has anthropic-claude-opus-4-7
    res = _invoke(
        runner, "agent", "register",
        "--provider", "Anthropic",
        "--model-family", "Claude",
        "--version", "opus-4-7",
    )
    assert res.exit_code != 0
