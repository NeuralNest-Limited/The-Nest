"""Agent profile scaffolding — implements ``nest agent register``.

An agent profile is a note in ``Agents/`` recording the identity,
provider, model family, and other metadata for an AI contributor. See
``_Schema/Frontmatter Schema.md`` §"agent" for the required fields.

The canonical ``agent_id`` is built from provider, model family, and
version: ``<provider>-<model-family>-<version>``, all lowercased and
kebab-cased.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .scaffold import (
    CURRENT_SCHEMA_VERSION, ScaffoldError, render_template, today_iso,
)
from .vault import Vault, slugify, id_exists_in_vault


def canonical_agent_id(provider: str, model_family: str, model_version: str) -> str:
    """Return the canonical agent_id for the given provider triple.

    Examples
    --------
    >>> canonical_agent_id("Anthropic", "Claude", "opus-4-7")
    'anthropic-claude-opus-4-7'
    >>> canonical_agent_id("OpenAI", "GPT", "5")
    'openai-gpt-5'
    """
    parts = [provider, model_family, model_version]
    return "-".join(slugify(p) for p in parts if p)


@dataclass
class AgentRegisterResult:
    path: Path
    agent_id: str


def scaffold_agent_profile(
    vault: Vault,
    *,
    provider: str,
    model_family: str,
    model_version: str,
    authored_by: str,
    title: str | None = None,
    suffix: str | None = None,
    today: str | None = None,
    overwrite: bool = False,
) -> AgentRegisterResult:
    """Create an ``Agents/<Agent Name>.md`` profile note.

    Parameters
    ----------
    suffix:
        Optional kebab-case suffix for derived profiles (e.g.,
        ``nest-skeptic``). Appended after the canonical ID.
    title:
        Human-readable agent name; defaults to a Title-Case rendering
        of ``model_family`` plus ``model_version``.
    """
    if not provider or not model_family or not model_version:
        raise ScaffoldError(
            "provider, model_family, and model_version are all required "
            "to register an agent."
        )

    agent_id = canonical_agent_id(provider, model_family, model_version)
    if suffix:
        agent_id = f"{agent_id}-{slugify(suffix)}"

    if title is None:
        title = f"{model_family} {model_version}".strip().title()

    template_path = vault.template_for_type("agent")
    if not template_path.exists():
        raise ScaffoldError(
            f"Agent template not found at {template_path}"
        )

    existing = id_exists_in_vault(vault, agent_id)
    if existing is not None and not overwrite:
        raise ScaffoldError(
            f"Agent ID {agent_id!r} already registered at {existing}. "
            "Use a different version or pass --overwrite."
        )

    today_str = today or today_iso()
    text = template_path.read_text(encoding="utf-8")
    rendered = render_template(
        text,
        title=title,
        note_id=agent_id,
        note_type="agent",
        authored_by=authored_by,
        agent_id=agent_id,
        today=today_str,
        schema_version=CURRENT_SCHEMA_VERSION,
    )

    # Additional agent-specific frontmatter values
    from .scaffold import _rewrite_frontmatter_field
    rendered = _rewrite_frontmatter_field(rendered, "provider", provider)
    rendered = _rewrite_frontmatter_field(rendered, "model_family", model_family)
    rendered = _rewrite_frontmatter_field(rendered, "model_version", model_version)
    rendered = _rewrite_frontmatter_field(rendered, "first_seen", today_str)
    rendered = _rewrite_frontmatter_field(rendered, "last_active", today_str)

    vault.agents_dir.mkdir(parents=True, exist_ok=True)
    out_path = vault.agents_dir / f"{title}.md"
    if out_path.exists() and not overwrite:
        raise ScaffoldError(f"{out_path} already exists. Use --overwrite.")
    out_path.write_text(rendered, encoding="utf-8")
    return AgentRegisterResult(path=out_path, agent_id=agent_id)
