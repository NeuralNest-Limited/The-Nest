"""Git operations — staging, committing, pushing.

Uses GitPython when available, falls back to ``git`` subprocess.
Commit messages follow ``_Meta/Git Commit Conventions.md``:

::

    <type>(<scope>): <subject>

    <body>

    Session: <session-id>
    Author-agent: <model-id>
"""

from __future__ import annotations

import os
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path


@dataclass
class CommitResult:
    """Result of staging + committing a single file."""

    sha: str
    message_subject: str
    pushed: bool = False


class GitError(RuntimeError):
    """Raised when a git operation fails."""


def _run_git(cwd: Path, *args: str) -> str:
    """Run ``git`` with the given arguments. Returns trimmed stdout."""
    if shutil.which("git") is None:
        raise GitError("`git` not found in PATH. Install git to use this CLI.")
    completed = subprocess.run(
        ["git", *args],
        cwd=str(cwd),
        capture_output=True,
        text=True,
        check=False,
    )
    if completed.returncode != 0:
        raise GitError(
            f"git {' '.join(args)} failed (exit {completed.returncode}):\n"
            f"stdout: {completed.stdout}\nstderr: {completed.stderr}"
        )
    return completed.stdout.strip()


def is_git_repo(path: Path) -> bool:
    """Return True if *path* is inside a git work tree."""
    try:
        _run_git(path, "rev-parse", "--is-inside-work-tree")
        return True
    except GitError:
        return False


def build_commit_message(
    *,
    commit_type: str,
    scope: str | None,
    subject: str,
    body: str | None = None,
    session_id: str | None = None,
    author_agent: str | None = None,
) -> str:
    """Compose a commit message per Git Commit Conventions.

    Subject is forced to imperative-style by leaving it to the caller;
    we just enforce length and structure.
    """
    if not commit_type:
        raise ValueError("commit_type is required")
    if not subject:
        raise ValueError("subject is required")
    header = f"{commit_type}({scope}): {subject}" if scope else f"{commit_type}: {subject}"
    # Per conventions, subject line ≤ 72 chars — warn (we don't truncate).
    parts: list[str] = [header]
    if body:
        parts.append("")
        parts.append(body.strip())
    trailers: list[str] = []
    if session_id:
        trailers.append(f"Session: {session_id}")
    if author_agent:
        trailers.append(f"Author-agent: {author_agent}")
    if trailers:
        parts.append("")
        parts.extend(trailers)
    return "\n".join(parts) + "\n"


def stage_and_commit(
    repo_root: Path,
    files: list[Path],
    *,
    commit_type: str,
    scope: str | None,
    subject: str,
    body: str | None = None,
    session_id: str | None = None,
    author_agent: str | None = None,
) -> CommitResult:
    """Stage *files* and commit them with a conventional message.

    Returns the resulting :class:`CommitResult`. Raises
    :class:`GitError` on failure (e.g., nothing to commit, or git
    refuses the operation).
    """
    if not files:
        raise GitError("No files specified to commit.")
    for f in files:
        rel = _relative_to(repo_root, f)
        _run_git(repo_root, "add", "--", str(rel))

    msg = build_commit_message(
        commit_type=commit_type,
        scope=scope,
        subject=subject,
        body=body,
        session_id=session_id,
        author_agent=author_agent,
    )

    # Use --file to handle multi-line message safely
    msg_file = repo_root / ".git" / ".NEST_CLI_COMMIT_MSG"
    msg_file.parent.mkdir(parents=True, exist_ok=True)
    msg_file.write_text(msg, encoding="utf-8")
    try:
        _run_git(repo_root, "commit", "-F", str(msg_file))
    finally:
        try:
            msg_file.unlink()
        except OSError:
            pass

    sha = _run_git(repo_root, "rev-parse", "--short", "HEAD")
    return CommitResult(sha=sha, message_subject=subject)


def push(repo_root: Path, *, remote: str = "origin", branch: str | None = None) -> str:
    """Push the current branch to *remote*. Returns git stdout."""
    args = ["push", remote]
    if branch:
        args.append(branch)
    return _run_git(repo_root, *args)


def current_branch(repo_root: Path) -> str:
    """Return the current branch name."""
    return _run_git(repo_root, "rev-parse", "--abbrev-ref", "HEAD")


def collect_session_commits(repo_root: Path, session_id: str) -> list[str]:
    """Return short SHAs of commits whose body contains ``Session: <id>``."""
    out = _run_git(
        repo_root,
        "log",
        "--all",
        "--pretty=format:%h%x09%B%x00",
        f"--grep=Session: {session_id}",
    )
    if not out:
        return []
    shas: list[str] = []
    for entry in out.split("\x00"):
        entry = entry.strip()
        if not entry:
            continue
        first_line = entry.split("\n", 1)[0]
        if "\t" in first_line:
            sha = first_line.split("\t", 1)[0].strip()
            if sha and sha not in shas:
                shas.append(sha)
    return shas


def _relative_to(root: Path, path: Path) -> Path:
    """Return *path* expressed relative to *root* if possible."""
    try:
        return path.resolve().relative_to(root.resolve())
    except ValueError:
        return path
