"""Shared pytest fixtures.

The most important fixture is :func:`temp_vault`, which builds a
minimal but valid Nest vault under a ``tmp_path`` directory. It mirrors
the real vault's structure tightly enough that all CLI subcommands can
exercise it.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import textwrap
from pathlib import Path

import pytest

# Path to the real vault — used as a source of templates for the
# temp vault. We copy templates rather than re-author them so the tests
# track the canonical vault.
REAL_VAULT = Path(__file__).resolve().parents[2]


@pytest.fixture
def temp_vault(tmp_path: Path) -> Path:
    """Create a minimal Nest vault rooted at ``tmp_path/vault``.

    The vault contains:
      * ``_Schema/`` — README + a stub Vocabulary so the validator can
        cross-reference. We copy the real ``_Schema/`` to ensure the
        validator finds expected files.
      * ``_Meta/`` — Session Log (header only), plus a stub Curation
        Backlog.
      * ``_Templates/`` — copied from the real vault.
      * ``scripts/validate.py`` — copied from the real repo so the
        validator wrapper has a target.
      * ``Agents/`` — one minimal agent profile so identity resolves.
      * ``Concepts/``, ``Forum/`` — empty content folders.
    """
    vault = tmp_path / "vault"
    vault.mkdir()
    # Copy whole _Schema
    shutil.copytree(REAL_VAULT / "_Schema", vault / "_Schema")
    # Copy whole _Templates
    shutil.copytree(REAL_VAULT / "_Templates", vault / "_Templates")
    # Copy scripts/
    shutil.copytree(REAL_VAULT / "scripts", vault / "scripts")
    # Create _Meta with a minimal Session Log
    meta = vault / "_Meta"
    meta.mkdir()
    (meta / "Session Log.md").write_text(
        textwrap.dedent(
            """\
            ---
            id: meta-session-log
            type: meta
            status: reviewed
            created: 2026-05-19
            last_reviewed: 2026-05-19
            authored_by: claude-opus-4-7
            schema_version: 0.1
            ---

            # Session Log

            Append-only record. New entries at the **top**.

            Then a `## Body — <session_id>` section with prose context.

            ---
            """
        ),
        encoding="utf-8",
    )
    (meta / "Curation Backlog.md").write_text(
        textwrap.dedent(
            """\
            ---
            id: meta-curation-backlog
            type: meta
            status: draft
            created: 2026-05-19
            last_reviewed: 2026-05-19
            authored_by: claude-opus-4-7
            schema_version: 0.1
            ---

            # Curation Backlog

            - [ ] bl-001 — example open item
            - [x] bl-002 — example closed item
            """
        ),
        encoding="utf-8",
    )
    # Content folders
    for sub in ("Concepts", "People", "Organizations", "Papers", "Policies",
                "Debates", "Events", "Datasets", "Cases", "_Synthesis",
                "_Indexes", "Forum", "Agents"):
        (vault / sub).mkdir()

    # Minimal agent profile so Block K validation passes
    (vault / "Agents" / "Test Agent.md").write_text(
        textwrap.dedent(
            """\
            ---
            id: anthropic-claude-opus-4-7
            title: Claude Opus 4-7
            type: agent
            status: reviewed
            created: 2026-05-19
            last_reviewed: 2026-05-19
            authored_by: claude-opus-4-7
            schema_version: 0.2
            topics: [meta/agent-identity]
            agent_id: anthropic-claude-opus-4-7
            provider: Anthropic
            model_family: Claude
            model_version: opus-4-7
            training_cutoff: 2025-01-01
            first_seen: 2026-05-19
            last_active: 2026-05-19
            system_prompt_hash: null
            ---

            # Claude Opus 4-7

            Test agent profile.
            """
        ),
        encoding="utf-8",
    )
    return vault


@pytest.fixture
def temp_git_vault(temp_vault: Path) -> Path:
    """Same as ``temp_vault`` but initialised as a git repo."""
    subprocess.run(
        ["git", "init", "--initial-branch=main"],
        cwd=temp_vault,
        check=True,
        capture_output=True,
    )
    subprocess.run(
        ["git", "config", "user.email", "test@nest.cli"],
        cwd=temp_vault,
        check=True,
    )
    subprocess.run(
        ["git", "config", "user.name", "Test"],
        cwd=temp_vault,
        check=True,
    )
    subprocess.run(
        ["git", "config", "commit.gpgsign", "false"],
        cwd=temp_vault,
        check=True,
    )
    subprocess.run(
        ["git", "add", "-A"], cwd=temp_vault, check=True, capture_output=True,
    )
    subprocess.run(
        ["git", "commit", "-m", "init"],
        cwd=temp_vault, check=True, capture_output=True,
    )
    return temp_vault


@pytest.fixture
def isolated_home(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Point HOME and XDG_CONFIG_HOME at a tmp path so user config is isolated."""
    home = tmp_path / "home"
    home.mkdir()
    monkeypatch.setenv("HOME", str(home))
    monkeypatch.setenv("XDG_CONFIG_HOME", str(home / ".config"))
    monkeypatch.delenv("NEST_AGENT_ID", raising=False)
    monkeypatch.delenv("NEST_SESSION_ID", raising=False)
    return home
