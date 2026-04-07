#!/usr/bin/env python3
"""Module that provides a multiplier factory function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by the multiplier."""
    def multiply(number: float) -> float:
        return multiplier * number
    return multiply
