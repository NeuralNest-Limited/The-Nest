"""Wrapper around the existing ``scripts/validate.py``.

Per Roadmap §5 ("DO NOT REINVENT VALIDATION"), this module shells out
to the validator that already exists in the vault rather than
re-implementing the rule set.

We invoke the validator as a subprocess with the same argument shape
the user would pass on the command line. The subprocess's stdout, exit
code, and stderr are returned to the caller so the ``nest validate``
subcommand can surface them faithfully.
"""

from __future__ import annotations

import shlex
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from .vault import Vault


class ValidatorMissingError(RuntimeError):
    """Raised when ``scripts/validate.py`` is not present in the vault."""


@dataclass
class ValidationResult:
    """Result of running the validator.

    Attributes
    ----------
    exit_code:
        ``0`` for clean, ``1`` for WARN, ``2`` for ERROR (matches
        ``scripts/validate.py``).
    stdout:
        Whatever the validator printed to stdout (human-readable or
        JSON depending on ``json_output``).
    stderr:
        Validator stderr; usually empty.
    """

    exit_code: int
    stdout: str
    stderr: str

    @property
    def ok(self) -> bool:
        return self.exit_code == 0

    @property
    def has_errors(self) -> bool:
        return self.exit_code >= 2


def run_validator(
    vault: Vault,
    *,
    file: Path | None = None,
    strict: bool = False,
    json_output: bool = False,
    quiet: bool = False,
    python: str | None = None,
) -> ValidationResult:
    """Run the vault's ``scripts/validate.py``.

    Parameters
    ----------
    vault:
        The discovered vault.
    file:
        If set, validate just this single file. Otherwise validate the
        full vault.
    strict:
        Pass ``--strict`` to the validator.
    json_output:
        Pass ``--json`` for machine-readable output.
    quiet:
        Pass ``--quiet`` (errors only).
    python:
        Python interpreter to invoke (defaults to ``sys.executable``).
    """
    script = vault.validator_script
    if not script.exists():
        raise ValidatorMissingError(
            f"Validator not found at {script}. Has it been moved or removed? "
            "The CLI's `validate` subcommand depends on scripts/validate.py "
            "(Roadmap §7)."
        )

    interpreter = python or sys.executable
    cmd: list[str] = [interpreter, str(script)]
    if file is not None:
        cmd.extend(["--file", str(file)])
    else:
        cmd.append("--all")
    if strict:
        cmd.append("--strict")
    if json_output:
        cmd.append("--json")
    if quiet:
        cmd.append("--quiet")
    # Always pass --vault-root for determinism (the validator can
    # auto-detect, but the CLI already knows where the vault is).
    cmd.extend(["--vault-root", str(vault.root)])

    completed = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        check=False,
    )
    return ValidationResult(
        exit_code=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
    )


def render_command(
    vault: Vault, *, file: Path | None = None, strict: bool = False
) -> str:
    """Return the underlying command for diagnostic display.

    Used by ``--verbose`` modes so users can see the exact validator
    invocation if they want to debug discrepancies.
    """
    cmd = [sys.executable, str(vault.validator_script)]
    if file is not None:
        cmd.extend(["--file", str(file)])
    else:
        cmd.append("--all")
    if strict:
        cmd.append("--strict")
    cmd.extend(["--vault-root", str(vault.root)])
    return " ".join(shlex.quote(c) for c in cmd)
