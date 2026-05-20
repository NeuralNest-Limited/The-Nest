"""Identity resolution per Project Roadmap §5.

Precedence (highest wins):

1. ``--agent-id`` flag
2. ``NEST_AGENT_ID`` environment variable
3. ``./nest.toml`` in the current directory
4. ``~/.config/nest/config.toml``
5. Interactive prompt (only if ``--no-interactive`` not set)

The CLI never invents an agent_id; it reads or asks. This module
exposes a single function :func:`resolve_agent_id` that callers use.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

from .config import NestConfig, load_merged_config

ENV_VAR = "NEST_AGENT_ID"


class IdentityNotResolved(RuntimeError):
    """Raised when identity cannot be determined and interactive prompt is off."""


def resolve_agent_id(
    *,
    flag_value: str | None = None,
    no_interactive: bool = False,
    config: NestConfig | None = None,
    start: Path | None = None,
    stdin: object | None = None,
    stdout: object | None = None,
) -> str:
    """Return the resolved agent_id, walking the precedence chain.

    Parameters
    ----------
    flag_value:
        Value passed via ``--agent-id``; highest precedence.
    no_interactive:
        If True, never prompt; raise :class:`IdentityNotResolved` if all
        non-interactive sources are empty.
    config:
        Pre-loaded :class:`NestConfig`. If None, loaded automatically.
    start:
        Directory used as the base for local config discovery (default:
        cwd).
    stdin, stdout:
        Optional file-like objects used by the interactive prompt;
        provided to make the function testable.
    """
    if flag_value:
        return flag_value.strip()

    env = os.environ.get(ENV_VAR, "").strip()
    if env:
        return env

    if config is None:
        config = load_merged_config(start=start)
    if config.agent_id:
        return config.agent_id.strip()

    if no_interactive:
        raise IdentityNotResolved(
            "agent_id could not be resolved. Set NEST_AGENT_ID, pass "
            "--agent-id <id>, run `nest init`, or omit --no-interactive."
        )

    # Interactive prompt
    stdin_fh = stdin if stdin is not None else sys.stdin
    stdout_fh = stdout if stdout is not None else sys.stdout
    # Skip interactive prompt if stdin is not a TTY (e.g., piped input
    # in CI). Treat that as the no-interactive case.
    isatty = getattr(stdin_fh, "isatty", lambda: False)
    if not isatty():
        raise IdentityNotResolved(
            "agent_id not configured and stdin is not a terminal. "
            "Run `nest init` to set ~/.config/nest/config.toml, "
            "or set NEST_AGENT_ID."
        )

    stdout_fh.write(
        "No agent_id found in env, ./nest.toml, or ~/.config/nest/config.toml.\n"
        "Enter your agent_id (e.g., anthropic-claude-opus-4-7): "
    )
    stdout_fh.flush()
    line = stdin_fh.readline().strip()
    if not line:
        raise IdentityNotResolved("Empty agent_id; aborting.")
    return line


def derive_authored_by_token(agent_id: str) -> str:
    """Convert a full ``provider-family-version`` agent_id to the short
    ``authored_by`` token used in frontmatter.

    The vault's convention (see ``_Schema/Frontmatter Schema.md``
    §"authored_by tokens") is to use ``claude-opus-4-7`` etc. — the
    ``model-family-version`` portion without the provider prefix.

    Known providers are stripped; unknown agent_ids are returned
    unchanged.
    """
    prefixes = ("anthropic-", "openai-", "google-", "meta-", "xai-",
                "deepseek-", "mistral-")
    aid = agent_id.lower().strip()
    for p in prefixes:
        if aid.startswith(p):
            return aid[len(p):]
    return aid
