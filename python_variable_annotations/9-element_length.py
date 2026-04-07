#!/usr/bin/env python3
"""Module for annotating iterable objects with their lengths."""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples containing each element and its length."""
    return [(i, len(i)) for i in lst]
