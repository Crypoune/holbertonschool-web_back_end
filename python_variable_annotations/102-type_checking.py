#!/usr/bin/env python3
"""iterable object zoomed in with type checking"""
from typing import Tuple, List

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """Return a list with each element of the tuple repeated 'factor' times."""
    zoomed_in: List[int] = [item for item in lst for _ in range(factor)]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))
zoom_3x = zoom_array(tuple(array), int(3.0))
