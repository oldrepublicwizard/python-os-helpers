"""Fallback logger when loggerplus is not installed."""
from __future__ import annotations
import logging

class RobustLogger:
    def __new__(cls, *args, **kwargs):
        return logging.getLogger("python_os_helpers")

def format_exception_with_variables(exc, *args, **kwargs):
    return str(exc)
