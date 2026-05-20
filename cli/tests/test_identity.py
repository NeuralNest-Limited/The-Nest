"""Tests for the identity resolution chain."""

from __future__ import annotations

import io
from pathlib import Path

import pytest

from nest_cli.config import NestConfig, write_user_config
from nest_cli.identity import (
    ENV_VAR, IdentityNotResolved, derive_authored_by_token,
    resolve_agent_id,
)


# ----- precedence happy path ----------------------------------------

def test_flag_value_takes_precedence(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv(ENV_VAR, "from-env")
    aid = resolve_agent_id(flag_value="from-flag", no_interactive=True)
    assert aid == "from-flag"


def test_env_var_used_when_no_flag(
    monkeypatch: pytest.MonkeyPatch, isolated_home: Path
) -> None:
    monkeypatch.setenv(ENV_VAR, "from-env")
    aid = resolve_agent_id(no_interactive=True)
    assert aid == "from-env"


def test_local_config_used_when_no_env(
    isolated_home: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.chdir(tmp_path)
    (tmp_path / "nest.toml").write_text(
        '[agent]\nagent_id = "local-aid"\n', encoding="utf-8"
    )
    aid = resolve_agent_id(no_interactive=True)
    assert aid == "local-aid"


def test_user_config_used_when_no_local(
    isolated_home: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    write_user_config(NestConfig(agent_id="user-aid"))
    monkeypatch.chdir(tmp_path)
    aid = resolve_agent_id(no_interactive=True)
    assert aid == "user-aid"


def test_interactive_prompt_used_when_no_other_source(
    isolated_home: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.chdir(tmp_path)

    class TTYIn(io.StringIO):
        def isatty(self) -> bool:  # type: ignore[override]
            return True

    stdin = TTYIn("prompted-aid\n")
    stdout = io.StringIO()
    aid = resolve_agent_id(stdin=stdin, stdout=stdout)
    assert aid == "prompted-aid"
    assert "Enter your agent_id" in stdout.getvalue()


# ----- failure modes -------------------------------------------------

def test_no_interactive_raises_when_no_source(
    isolated_home: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.chdir(tmp_path)
    with pytest.raises(IdentityNotResolved):
        resolve_agent_id(no_interactive=True)


def test_non_tty_stdin_raises(
    isolated_home: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.chdir(tmp_path)
    stdin = io.StringIO("anything\n")  # not a TTY
    stdout = io.StringIO()
    with pytest.raises(IdentityNotResolved):
        resolve_agent_id(stdin=stdin, stdout=stdout)


def test_empty_prompted_input_raises(
    isolated_home: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.chdir(tmp_path)

    class TTYIn(io.StringIO):
        def isatty(self) -> bool:  # type: ignore[override]
            return True

    stdin = TTYIn("\n")
    stdout = io.StringIO()
    with pytest.raises(IdentityNotResolved):
        resolve_agent_id(stdin=stdin, stdout=stdout)


def test_flag_value_strips_whitespace(monkeypatch: pytest.MonkeyPatch) -> None:
    aid = resolve_agent_id(flag_value="  spaced-id  ", no_interactive=True)
    assert aid == "spaced-id"


# ----- derive_authored_by_token --------------------------------------

@pytest.mark.parametrize(
    "agent_id,expected",
    [
        ("anthropic-claude-opus-4-7", "claude-opus-4-7"),
        ("openai-gpt-5", "gpt-5"),
        ("google-gemini-3-pro", "gemini-3-pro"),
        ("meta-llama-4", "llama-4"),
        ("unknown-foo-bar", "unknown-foo-bar"),
        ("ANTHROPIC-CLAUDE-OPUS-4-7", "claude-opus-4-7"),
    ],
)
def test_derive_authored_by_token(agent_id: str, expected: str) -> None:
    assert derive_authored_by_token(agent_id) == expected
