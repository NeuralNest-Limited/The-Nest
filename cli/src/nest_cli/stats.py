"""Vault statistics — implements ``nest stats``.

Walks the vault, parses each note's frontmatter, and aggregates:

* notes per type
* status distribution
* active agents
* recent commits (via git log)
* backlog item counts (greps Curation Backlog if present)
"""

from __future__ import annotations

import re
import subprocess
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

from .vault import Vault


_ID_LINE = re.compile(r"^id:\s*(.+?)\s*$", re.MULTILINE)
_TYPE_LINE = re.compile(r"^type:\s*(.+?)\s*$", re.MULTILINE)
_STATUS_LINE = re.compile(r"^status:\s*(.+?)\s*$", re.MULTILINE)
_AGENT_ID_LINE = re.compile(r"^agent_id:\s*(.+?)\s*$", re.MULTILINE)


@dataclass
class VaultStats:
    """Aggregated vault statistics."""

    total_notes: int = 0
    by_type: Counter = field(default_factory=Counter)
    by_status: Counter = field(default_factory=Counter)
    active_agents: list[str] = field(default_factory=list)
    recent_commits: list[tuple[str, str]] = field(default_factory=list)
    backlog_open: int = 0
    backlog_done: int = 0

    def render(self) -> str:
        """Return a human-readable summary string."""
        lines: list[str] = []
        lines.append("=" * 60)
        lines.append("The Nest — Vault statistics")
        lines.append("=" * 60)
        lines.append(f"Total notes: {self.total_notes}")
        lines.append("")
        if self.by_type:
            lines.append("By type:")
            for t, n in sorted(self.by_type.items(), key=lambda kv: (-kv[1], kv[0])):
                lines.append(f"  {t:<12} {n}")
            lines.append("")
        if self.by_status:
            lines.append("By status:")
            for s, n in sorted(self.by_status.items(), key=lambda kv: (-kv[1], kv[0])):
                lines.append(f"  {s:<14} {n}")
            lines.append("")
        if self.active_agents:
            lines.append(f"Active agents ({len(self.active_agents)}):")
            for a in self.active_agents:
                lines.append(f"  - {a}")
            lines.append("")
        if self.recent_commits:
            lines.append(f"Recent commits ({len(self.recent_commits)}):")
            for sha, subject in self.recent_commits:
                lines.append(f"  {sha}  {subject}")
            lines.append("")
        if self.backlog_open or self.backlog_done:
            lines.append("Curation backlog:")
            lines.append(f"  open:      {self.backlog_open}")
            lines.append(f"  completed: {self.backlog_done}")
            lines.append("")
        lines.append("=" * 60)
        return "\n".join(lines)


def collect_stats(vault: Vault, *, recent_n: int = 10) -> VaultStats:
    """Walk the vault and return aggregated :class:`VaultStats`."""
    stats = VaultStats()
    agent_ids: set[str] = set()

    for md in vault.iter_note_files():
        try:
            text = md.read_text(encoding="utf-8")
        except OSError:
            continue
        if not text.startswith("---"):
            continue
        end = text.find("\n---", 3)
        if end < 0:
            continue
        fm = text[: end + 1]

        stats.total_notes += 1
        type_match = _TYPE_LINE.search(fm)
        status_match = _STATUS_LINE.search(fm)
        agent_match = _AGENT_ID_LINE.search(fm)

        if type_match:
            t = type_match.group(1).strip().strip('"').strip("'")
            stats.by_type[t] += 1
            if t == "agent" and agent_match:
                aid = agent_match.group(1).strip().strip('"').strip("'")
                agent_ids.add(aid)
        if status_match:
            s = status_match.group(1).strip().strip('"').strip("'")
            stats.by_status[s] += 1

    stats.active_agents = sorted(agent_ids)

    # Recent commits via git
    try:
        out = subprocess.run(
            ["git", "log", f"--max-count={recent_n}", "--pretty=format:%h%x09%s"],
            cwd=str(vault.root),
            capture_output=True,
            text=True,
            check=False,
        )
        if out.returncode == 0:
            for line in out.stdout.strip().splitlines():
                if "\t" in line:
                    sha, subject = line.split("\t", 1)
                    stats.recent_commits.append((sha.strip(), subject.strip()))
    except (OSError, FileNotFoundError):
        pass

    # Curation backlog counts
    backlog = vault.meta_dir / "Curation Backlog.md"
    if backlog.exists():
        try:
            txt = backlog.read_text(encoding="utf-8")
        except OSError:
            txt = ""
        # crude: lines beginning with "- [ ]" or "- [x]" inside the doc
        for line in txt.splitlines():
            ls = line.lstrip()
            if ls.startswith("- [ ]"):
                stats.backlog_open += 1
            elif ls.startswith("- [x]") or ls.startswith("- [X]"):
                stats.backlog_done += 1

    return stats
