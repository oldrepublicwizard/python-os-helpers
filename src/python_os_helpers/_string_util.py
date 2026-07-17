from __future__ import annotations

def is_non_empty_string(value: str | None) -> bool:
    return isinstance(value, str) and bool(value.strip())

def normalize_string(value: str | None) -> str:
    return "" if value is None else str(value)
