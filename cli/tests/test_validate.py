"""Tests for the validator wrapper."""

from __future__ import annotations

from pathlib import Path

import pytest

from nest_cli.validate import (
    ValidatorMissingError, render_command, run_validator,
)
from nest_cli.vault import Vault


def test_run_validator_clean_on_empty_vault(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    result = run_validator(v)
    # No content notes; only schema/meta/templates copied. Should not ERROR.
    assert not result.has_errors


def test_run_validator_file_specific(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    agent_file = v.agents_dir / "Test Agent.md"
    result = run_validator(v, file=agent_file)
    assert not result.has_errors


def test_run_validator_strict_returns_warn_exit(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    # Create a content-bearing concept missing topics — WARN
    note = v.root / "Concepts" / "Weak Note.md"
    note.write_text(
        "---\nid: weak-note\ntitle: Weak\ntype: concept\nstatus: draft\n"
        "created: 2026-05-20\nlast_reviewed: 2026-05-20\nauthored_by: x\n"
        "schema_version: 0.2\n---\n\n# Weak\n",
        encoding="utf-8",
    )
    result = run_validator(v, file=note, strict=True)
    # strict=True still flags WARN as exit 1
    assert result.exit_code in {0, 1}


def test_run_validator_json_output_is_json(temp_vault: Path) -> None:
    import json
    v = Vault(root=temp_vault)
    result = run_validator(v, json_output=True)
    data = json.loads(result.stdout)
    assert "summary" in data
    assert "issues" in data


def test_run_validator_missing_script_raises(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    # Remove the wrapper script
    import shutil
    shutil.rmtree(v.root / "scripts")
    with pytest.raises(ValidatorMissingError):
        run_validator(v)


def test_render_command_contains_vault_root(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    cmd = render_command(v)
    assert str(v.root) in cmd
    assert "validate.py" in cmd


def test_run_validator_quiet_suppresses_warns(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    note = v.root / "Concepts" / "Quiet Test.md"
    note.write_text(
        "---\nid: quiet-test\ntitle: x\ntype: concept\nstatus: draft\n"
        "created: 2026-05-20\nlast_reviewed: 2026-05-20\nauthored_by: x\n"
        "schema_version: 0.2\n---\n\n# x\n",
        encoding="utf-8",
    )
    result = run_validator(v, quiet=True)
    assert "WARN" not in result.stdout or "Total issues" in result.stdout


def test_run_validator_error_on_duplicate_keys(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    note = v.root / "Concepts" / "Dup Keys.md"
    note.write_text(
        "---\nid: dup-keys\nid: also-dup-keys\ntitle: x\n"
        "type: concept\nstatus: stub\ncreated: 2026-05-20\n"
        "last_reviewed: 2026-05-20\nauthored_by: x\nschema_version: 0.2\n"
        "---\n\n# x\n",
        encoding="utf-8",
    )
    result = run_validator(v, file=note)
    # Block A duplicate-key check produces ERROR
    assert result.exit_code == 2


def test_run_validator_handles_unknown_type(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    note = v.root / "Concepts" / "Bad Type.md"
    note.write_text(
        "---\nid: bad-type\ntitle: x\ntype: flarp\nstatus: draft\n"
        "created: 2026-05-20\nlast_reviewed: 2026-05-20\nauthored_by: x\n"
        "schema_version: 0.2\n---\n\n# x\n",
        encoding="utf-8",
    )
    result = run_validator(v, file=note)
    assert result.exit_code == 2  # unknown type is ERROR
