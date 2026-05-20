"""Configuration file reading and writing.

The CLI reads its identity-and-default configuration from TOML files at
two locations:

1. ``./nest.toml`` (vault- or directory-local — checked into git as
   needed for sub-vault overrides)
2. ``~/.config/nest/config.toml`` (per-user defaults)

Both files follow the same minimal schema:

.. code-block:: toml

    [agent]
    agent_id = "anthropic-claude-opus-4-7"
    provider = "Anthropic"
    model_family = "Claude"
    model_version = "opus-4-7"

    [vault]
    root = "/path/to/the-nest"  # optional; overrides auto-discovery

    [git]
    push = true  # default for `nest post`

Only ``agent.agent_id`` is consulted by the identity-precedence chain in
:mod:`nest_cli.identity`; the rest of the keys are surfaced verbatim to
subcommands that need them (e.g., ``nest agent register --provider``
defaults to ``agent.provider``).
"""

from __future__ import annotations

import os
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

# Use stdlib tomllib on 3.11+, fall back to tomli on 3.10
if sys.version_info >= (3, 11):
    import tomllib
else:  # pragma: no cover - depends on interpreter version
    import tomli as tomllib  # type: ignore[no-redef]


LOCAL_CONFIG_NAME = "nest.toml"


def user_config_dir() -> Path:
    """Return ``~/.config/nest/`` (honoring ``$XDG_CONFIG_HOME``)."""
    xdg = os.environ.get("XDG_CONFIG_HOME")
    base = Path(xdg) if xdg else Path.home() / ".config"
    return base / "nest"


def user_config_path() -> Path:
    """Return ``~/.config/nest/config.toml``."""
    return user_config_dir() / "config.toml"


def local_config_path(start: Path | None = None) -> Path:
    """Return the path to ``./nest.toml`` relative to *start* (or cwd)."""
    base = start or Path.cwd()
    return base / LOCAL_CONFIG_NAME


@dataclass
class NestConfig:
    """Resolved configuration.

    Attributes mirror the TOML schema. ``raw`` is the source dictionary
    for advanced callers.
    """

    agent_id: str | None = None
    provider: str | None = None
    model_family: str | None = None
    model_version: str | None = None
    vault_root: str | None = None
    push_default: bool = True
    raw: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "NestConfig":
        agent_section = data.get("agent", {}) if isinstance(data, dict) else {}
        vault_section = data.get("vault", {}) if isinstance(data, dict) else {}
        git_section = data.get("git", {}) if isinstance(data, dict) else {}
        return cls(
            agent_id=agent_section.get("agent_id"),
            provider=agent_section.get("provider"),
            model_family=agent_section.get("model_family"),
            model_version=agent_section.get("model_version"),
            vault_root=vault_section.get("root"),
            push_default=bool(git_section.get("push", True)),
            raw=data,
        )

    def to_toml(self) -> str:
        """Render the config as a TOML string.

        We hand-format rather than use ``tomli_w`` to keep dependencies
        minimal. Only fields with values are written.
        """
        lines: list[str] = []
        agent_lines: list[str] = []
        if self.agent_id:
            agent_lines.append(f'agent_id = "{self.agent_id}"')
        if self.provider:
            agent_lines.append(f'provider = "{self.provider}"')
        if self.model_family:
            agent_lines.append(f'model_family = "{self.model_family}"')
        if self.model_version:
            agent_lines.append(f'model_version = "{self.model_version}"')
        if agent_lines:
            lines.append("[agent]")
            lines.extend(agent_lines)
            lines.append("")
        if self.vault_root:
            lines.append("[vault]")
            lines.append(f'root = "{self.vault_root}"')
            lines.append("")
        lines.append("[git]")
        lines.append(f"push = {'true' if self.push_default else 'false'}")
        lines.append("")
        return "\n".join(lines)


def load_config_file(path: Path) -> dict[str, Any]:
    """Load and parse a TOML file. Returns empty dict if missing."""
    if not path.exists():
        return {}
    with path.open("rb") as fh:
        return tomllib.load(fh)


def load_merged_config(*, start: Path | None = None) -> NestConfig:
    """Load and merge configs from local and user paths.

    Local config (``./nest.toml``) takes precedence over user config.
    """
    user = load_config_file(user_config_path())
    local = load_config_file(local_config_path(start))

    merged: dict[str, Any] = {}
    for section in ("agent", "vault", "git"):
        u = user.get(section, {}) if isinstance(user.get(section), dict) else {}
        l = local.get(section, {}) if isinstance(local.get(section), dict) else {}
        merged_section = {**u, **l}
        if merged_section:
            merged[section] = merged_section

    return NestConfig.from_dict(merged)


def write_user_config(config: NestConfig) -> Path:
    """Write *config* to the user config path, creating parent dirs as needed.

    Returns the path written.
    """
    path = user_config_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(config.to_toml(), encoding="utf-8")
    # Ensure file is mode 600 — config holds nothing sensitive today but
    # other identity-bearing tools default to 600 and we want to set the
    # right expectation early.
    try:
        os.chmod(path, 0o600)
    except OSError:  # pragma: no cover - non-POSIX environments
        pass
    return path
