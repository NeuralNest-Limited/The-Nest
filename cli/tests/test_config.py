"""Tests for the TOML config layer."""

from __future__ import annotations

from pathlib import Path

import pytest

from nest_cli.config import (
    NestConfig, load_config_file, load_merged_config, local_config_path,
    user_config_dir, user_config_path, write_user_config,
)


# ----- NestConfig serialization -------------------------------------

def test_nestconfig_to_toml_includes_agent_section() -> None:
    cfg = NestConfig(agent_id="anthropic-claude-opus-4-7")
    out = cfg.to_toml()
    assert "[agent]" in out
    assert 'agent_id = "anthropic-claude-opus-4-7"' in out
    assert "[git]" in out


def test_nestconfig_to_toml_includes_provider_when_set() -> None:
    cfg = NestConfig(
        agent_id="anthropic-claude-opus-4-7",
        provider="Anthropic",
        model_family="Claude",
        model_version="opus-4-7",
    )
    out = cfg.to_toml()
    assert 'provider = "Anthropic"' in out
    assert 'model_family = "Claude"' in out
    assert 'model_version = "opus-4-7"' in out


def test_nestconfig_from_dict_handles_empty() -> None:
    cfg = NestConfig.from_dict({})
    assert cfg.agent_id is None
    assert cfg.push_default is True


def test_nestconfig_from_dict_reads_git_push_false() -> None:
    cfg = NestConfig.from_dict({"git": {"push": False}})
    assert cfg.push_default is False


# ----- file IO ------------------------------------------------------

def test_load_config_file_returns_empty_for_missing(tmp_path: Path) -> None:
    assert load_config_file(tmp_path / "absent.toml") == {}


def test_load_config_file_parses_existing(tmp_path: Path) -> None:
    p = tmp_path / "c.toml"
    p.write_text('[agent]\nagent_id = "x-y-z"\n', encoding="utf-8")
    data = load_config_file(p)
    assert data["agent"]["agent_id"] == "x-y-z"


def test_user_config_path_honors_xdg(
    isolated_home: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    expected = isolated_home / ".config" / "nest" / "config.toml"
    assert user_config_path() == expected


def test_write_user_config_creates_dirs(isolated_home: Path) -> None:
    cfg = NestConfig(agent_id="a-b-c")
    path = write_user_config(cfg)
    assert path.exists()
    assert "a-b-c" in path.read_text(encoding="utf-8")


def test_load_merged_local_overrides_user(
    isolated_home: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    user_cfg = NestConfig(agent_id="user-id")
    write_user_config(user_cfg)
    local = tmp_path / "nest.toml"
    local.write_text('[agent]\nagent_id = "local-id"\n', encoding="utf-8")
    monkeypatch.chdir(tmp_path)
    merged = load_merged_config()
    assert merged.agent_id == "local-id"


def test_load_merged_returns_user_when_no_local(
    isolated_home: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    user_cfg = NestConfig(agent_id="user-id")
    write_user_config(user_cfg)
    monkeypatch.chdir(tmp_path)
    merged = load_merged_config()
    assert merged.agent_id == "user-id"


def test_load_merged_handles_no_config_at_all(
    isolated_home: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.chdir(tmp_path)
    merged = load_merged_config()
    assert merged.agent_id is None


def test_write_user_config_sets_secure_permissions(isolated_home: Path) -> None:
    import os
    cfg = NestConfig(agent_id="x")
    path = write_user_config(cfg)
    mode = os.stat(path).st_mode & 0o777
    # Either 0o600 or 0o400-equivalent; we accept 0o600 specifically.
    assert mode == 0o600
