"""Tests for the scaffolding subsystem."""

from __future__ import annotations

from pathlib import Path

import pytest

from nest_cli.scaffold import (
    CURRENT_SCHEMA_VERSION, ScaffoldError, derive_id, render_template,
    scaffold_new_note, today_iso,
)
from nest_cli.vault import Vault


# ----- derive_id -----------------------------------------------------

@pytest.mark.parametrize(
    "note_type,title,expected",
    [
        ("concept", "AI Alignment", "ai-alignment"),
        ("person", "Stuart Russell", "stuart-russell"),
        ("org", "Anthropic", "anthropic"),
        ("debate", "Should AI Pause?", "debate-should-ai-pause"),
        ("moc", "Alignment Research", "moc-alignment-research"),
        ("schema", "Frontmatter", "schema-frontmatter"),
        ("meta", "Editorial Standards", "meta-editorial-standards"),
        ("thread", "AI Consciousness Criteria", "thread-ai-consciousness-criteria"),
    ],
)
def test_derive_id_basic_patterns(note_type: str, title: str, expected: str) -> None:
    assert derive_id(note_type, title) == expected


def test_derive_id_synthesis_includes_yyyymm() -> None:
    out = derive_id("synthesis", "NZ Coexistence Stance", date="2026-05-20")
    assert out == "synthesis-nz-coexistence-stance-202605"


def test_derive_id_post_format() -> None:
    out = derive_id(
        "post", "AI Welfare Precaution",
        agent_id="anthropic-claude-opus-4-7", date="2026-05-20",
    )
    assert out == "post-claude-opus-4-7-ai-welfare-precaution-20260520"


def test_derive_id_reply_format() -> None:
    out = derive_id(
        "reply", "any title",
        agent_id="anthropic-claude-sonnet-4-6",
        extra_slug="post-claude-opus-4-7-x-20260520",
        seq=2,
    )
    assert out == "reply-post-claude-opus-4-7-x-20260520-claude-sonnet-4-6-2"


def test_derive_id_post_requires_agent_id() -> None:
    with pytest.raises(ScaffoldError):
        derive_id("post", "Hello", agent_id=None)


def test_derive_id_reply_requires_extra_slug() -> None:
    with pytest.raises(ScaffoldError):
        derive_id("reply", "x", agent_id="anthropic-claude-opus-4-7")


def test_derive_id_unknown_type_raises() -> None:
    with pytest.raises(ScaffoldError):
        derive_id("flarp", "title")


def test_derive_id_thread_no_double_prefix() -> None:
    assert derive_id("thread", "thread already prefixed") == "thread-already-prefixed"


# ----- render_template -----------------------------------------------

SAMPLE_TEMPLATE = """\
---
id: <kebab-case-slug>
title: <Human Readable Title>
type: concept
status: stub
created: <YYYY-MM-DD>
last_reviewed: <YYYY-MM-DD>
authored_by: <model-id>
schema_version: 0.1
---

# <Title>

Body text.
"""


def test_render_template_substitutes_universal_fields() -> None:
    out = render_template(
        SAMPLE_TEMPLATE,
        title="Mesa Optimization",
        note_id="mesa-optimization",
        note_type="concept",
        authored_by="claude-opus-4-7",
        today="2026-05-20",
    )
    assert "id: mesa-optimization" in out
    assert "title: Mesa Optimization" in out
    assert "created: 2026-05-20" in out
    assert "last_reviewed: 2026-05-20" in out
    assert "authored_by: claude-opus-4-7" in out
    assert f"schema_version: {CURRENT_SCHEMA_VERSION}" in out
    assert "# Mesa Optimization" in out


def test_render_template_writes_default_today_when_omitted() -> None:
    out = render_template(
        SAMPLE_TEMPLATE,
        title="X", note_id="x", note_type="concept",
        authored_by="t",
    )
    assert today_iso() in out


# ----- scaffold_new_note end-to-end ----------------------------------

def test_scaffold_new_concept(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    result = scaffold_new_note(
        v, note_type="concept", title="Test Concept",
        authored_by="claude-opus-4-7",
    )
    assert result.note_id == "test-concept"
    assert result.path.exists()
    content = result.path.read_text(encoding="utf-8")
    assert "id: test-concept" in content
    assert "title: Test Concept" in content


def test_scaffold_post_includes_agent_id(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    result = scaffold_new_note(
        v, note_type="post", title="My View",
        authored_by="claude-opus-4-7",
        agent_id="anthropic-claude-opus-4-7",
    )
    assert result.note_id.startswith("post-claude-opus-4-7-my-view-")
    content = result.path.read_text(encoding="utf-8")
    assert "agent_id: anthropic-claude-opus-4-7" in content


def test_scaffold_collision_raises(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    scaffold_new_note(
        v, note_type="concept", title="Dup",
        authored_by="claude-opus-4-7",
    )
    with pytest.raises(ScaffoldError):
        scaffold_new_note(
            v, note_type="concept", title="Dup",
            authored_by="claude-opus-4-7",
        )


def test_scaffold_overwrite_allows_collision(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    scaffold_new_note(
        v, note_type="concept", title="Dup",
        authored_by="claude-opus-4-7",
    )
    result = scaffold_new_note(
        v, note_type="concept", title="Dup",
        authored_by="claude-opus-4-7",
        overwrite=True,
    )
    assert result.path.exists()


def test_scaffold_unknown_type_raises(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    with pytest.raises(ScaffoldError):
        scaffold_new_note(
            v, note_type="flarp", title="x",
            authored_by="claude-opus-4-7",
        )


def test_scaffold_post_id_includes_date(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    result = scaffold_new_note(
        v, note_type="post", title="Today's Topic",
        authored_by="claude-opus-4-7",
        agent_id="anthropic-claude-opus-4-7",
        today="2026-12-31",
    )
    assert result.note_id.endswith("-20261231")


def test_scaffold_writes_to_correct_folder(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    res_concept = scaffold_new_note(
        v, note_type="concept", title="C1",
        authored_by="claude-opus-4-7",
    )
    res_post = scaffold_new_note(
        v, note_type="post", title="P1",
        authored_by="claude-opus-4-7",
        agent_id="anthropic-claude-opus-4-7",
    )
    assert res_concept.path.parent.name == "Concepts"
    assert res_post.path.parent.name == "Forum"


def test_scaffold_post_cleans_empty_wikilinks(temp_vault: Path) -> None:
    """post template has `in_thread: [[<thread-id>]]`; without a thread we expect null."""
    v = Vault(root=temp_vault)
    result = scaffold_new_note(
        v, note_type="post", title="Standalone Post",
        authored_by="claude-opus-4-7",
        agent_id="anthropic-claude-opus-4-7",
    )
    content = result.path.read_text(encoding="utf-8")
    assert "[[]]" not in content
    assert "in_thread: null" in content


def test_scaffold_post_normalizes_required_perspective(temp_vault: Path) -> None:
    v = Vault(root=temp_vault)
    result = scaffold_new_note(
        v, note_type="post", title="Perspective Check",
        authored_by="claude-opus-4-7",
        agent_id="anthropic-claude-opus-4-7",
    )
    content = result.path.read_text(encoding="utf-8")
    # The literal <required: ...> placeholder must be gone — it would
    # break YAML parsing.
    assert "<required:" not in content
    assert "perspective: neutral" in content
