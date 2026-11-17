"""Unit tests for code-block locator helpers in ``app.utils.chat_helpers``."""

from __future__ import annotations

import pytest

from app.utils.chat_helpers import block_qualified_name, format_code_locator


@pytest.mark.parametrize(
    ("block", "expected"),
    [
        ({"code_metadata": {"qualified_name": "pkg.mod.fn"}}, "pkg.mod.fn"),
        ({}, ""),
        ({"code_metadata": "pkg.fn"}, ""),
        ({"code_metadata": {}}, ""),
        ({"code_metadata": {"qualified_name": ""}}, ""),
    ],
)
def test_block_qualified_name(block: dict[str, object], expected: str) -> None:
    assert block_qualified_name(block) == expected


@pytest.mark.parametrize(
    ("file_path", "qualified_name", "expected"),
    [
        ("src/app.py", "pkg.mod.fn", "src/app.py#pkg.mod.fn"),
        ("src/app.py", "", "src/app.py"),
        ("", "pkg.mod.fn", "pkg.mod.fn"),
        ("", "", ""),
    ],
)
def test_format_code_locator(
    file_path: str, qualified_name: str, expected: str
) -> None:
    assert format_code_locator(file_path, qualified_name) == expected
