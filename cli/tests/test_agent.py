"""Tests for the agent registration subsystem."""

from __future__ import annotations

from pathlib import Path

import pytest

from nest_cli.agent import canonical_agent_id, scaffold_agent_profile
from nest_cli.scaffold import ScaffoldError
from nest_cli.vault import Vault


# ----- canonical_agent_id -------------------------------------------

@pytest.mark.parametrize(
    "provider,family,version,expected",
    [
        ("Anthropic", "Claude", "opus-4-7", "anthropic-claude-opus-4-7"),
        ("OpenAI", "GPT", "5", "openai-gpt-5"),
        ("Google", "Gemini", "3 Pro", "google-gemini-3-pro"),
        ("Meta", "Llama", "4", "meta-llama-4"),
        ("xAI", "Grok", "3", "xai-grok-3"),
    ],
)
def test_canonical_agent_id(provider: str, family: str, version: str, expected: str) -> None:
    assert canonical_agent_id(provider, family, version) == expected


# ----- scaffold_agent_profile ---------------------------------------

def test_scaffold_agent_creates_file(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    result = scaffold_agent_profile(
        v,
        provider="OpenAI",
        model_family="GPT",
        model_version="5",
        authored_by="claude-opus-4-7",
    )
    assert result.path.exists()
    assert result.agent_id == "openai-gpt-5"
    content = result.path.read_text(encoding="utf-8")
    assert "agent_id: openai-gpt-5" in content
    assert "provider: OpenAI" in content
    assert "model_family: GPT" in content
    assert "model_version: 5" in content


def test_scaffold_agent_with_suffix(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    result = scaffold_agent_profile(
        v,
        provider="Anthropic",
        model_family="Claude",
        model_version="opus-4-7",
        authored_by="claude-opus-4-7",
        suffix="nest-skeptic",
        title="Claude Opus 4-7 Nest Skeptic",
    )
    assert result.agent_id == "anthropic-claude-opus-4-7-nest-skeptic"


def test_scaffold_agent_collision_raises(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    # temp_vault already has anthropic-claude-opus-4-7 fixture
    with pytest.raises(ScaffoldError):
        scaffold_agent_profile(
            v,
            provider="Anthropic",
            model_family="Claude",
            model_version="opus-4-7",
            authored_by="claude-opus-4-7",
        )


def test_scaffold_agent_missing_provider_raises(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    with pytest.raises(ScaffoldError):
        scaffold_agent_profile(
            v, provider="", model_family="GPT",
            model_version="5", authored_by="x",
        )


def test_scaffold_agent_first_seen_today(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    result = scaffold_agent_profile(
        v,
        provider="DeepSeek",
        model_family="DeepSeek",
        model_version="3",
        authored_by="claude-opus-4-7",
        today="2026-08-15",
    )
    content = result.path.read_text(encoding="utf-8")
    assert "first_seen: 2026-08-15" in content
    assert "last_active: 2026-08-15" in content


def test_scaffold_agent_default_title(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    result = scaffold_agent_profile(
        v,
        provider="xAI",
        model_family="Grok",
        model_version="3",
        authored_by="claude-opus-4-7",
    )
    # title derived from model_family + model_version, title-cased
    assert "Grok" in result.path.name
