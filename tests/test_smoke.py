"""Smoke import test."""

def test_import():
    from python_os_helpers import ensure_directory_exists, is_frozen
    assert callable(ensure_directory_exists)
