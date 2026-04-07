#!/usr/bin/env python3
"""iterable object Any"""
from typing import Any, Optional, Sequence


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Return the first element of a sequence, or None if empty."""
    if lst:
        return lst[0]
    return None
