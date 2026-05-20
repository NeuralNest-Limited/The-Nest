"""Tests for vault discovery + slugify + id-uniqueness helpers."""

from __future__ import annotations

from pathlib import Path

import pytest

from nest_cli.vault import (
    Vault, VaultNotFoundError, discover_vault, id_exists_in_vault,
    is_vault_root, slugify,
)


# ----- slugify -------------------------------------------------------

@pytest.mark.parametrize(
    "raw,expected",
    [
        ("Hello World", "hello-world"),
        ("AI Alignment", "ai-alignment"),
        ("  spaces and  more  ", "spaces-and-more"),
        ("Te Reo Māori", "te-reo-maori"),
        ("Already_kebab-case", "already-kebab-case"),
        ("CAPS!!!", "caps"),
        ("multi---dash", "multi-dash"),
        ("", ""),
        ("A/B/C", "a-b-c"),
        ("special_chars$%&#@", "special-chars"),
    ],
)
def test_slugify_normalizes_correctly(raw: str, expected: str) -> None:
    assert slugify(raw) == expected


# ----- vault discovery happy path -----------------------------------

def test_is_vault_root_true_for_temp_vault(temp_vault: Path) -> None:
    assert is_vault_root(temp_vault) is True


def test_is_vault_root_false_for_random_dir(tmp_path: Path) -> None:
    assert is_vault_root(tmp_path) is False


def test_is_vault_root_true_when_marker_file(tmp_path: Path) -> None:
    (tmp_path / ".nest-vault").touch()
    assert is_vault_root(tmp_path) is True


def test_discover_vault_finds_from_root(temp_vault: Path) -> None:
    v = discover_vault(temp_vault)
    assert v.root == temp_vault


def test_discover_vault_walks_up_from_subdir(temp_vault: Path) -> None:
    inner = temp_vault / "Concepts" / "deep" / "subdir"
    inner.mkdir(parents=True)
    v = discover_vault(inner)
    assert v.root == temp_vault


# ----- vault discovery failure modes --------------------------------

def test_discover_vault_raises_outside(tmp_path: Path) -> None:
    other = tmp_path / "not-a-vault"
    other.mkdir()
    with pytest.raises(VaultNotFoundError):
        discover_vault(other, max_depth=3)


def test_discover_vault_raises_on_filesystem_root() -> None:
    with pytest.raises(VaultNotFoundError):
        discover_vault(Path("/"), max_depth=2)


# ----- Vault helper methods -----------------------------------------

def test_vault_folder_for_type(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    assert v.folder_for_type("concept") == temp_vault / "Concepts"
    assert v.folder_for_type("post") == temp_vault / "Forum"
    assert v.folder_for_type("agent") == temp_vault / "Agents"


def test_vault_folder_for_unknown_type_raises(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    with pytest.raises(ValueError):
        v.folder_for_type("flarp")


def test_vault_template_for_type(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    assert v.template_for_type("concept").name == "Concept Template.md"


# ----- id_exists_in_vault -------------------------------------------

def test_id_exists_finds_agent(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    found = id_exists_in_vault(v, "anthropic-claude-opus-4-7")
    assert found is not None
    assert found.name == "Test Agent.md"


def test_id_exists_returns_none_for_missing_id(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    assert id_exists_in_vault(v, "totally-missing-id-xyz") is None
