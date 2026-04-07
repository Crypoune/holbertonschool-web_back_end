#!/usr/bin/env python3
"""Module that provides a type-annotated concat function."""


def concat(str1: str, str2: str) -> str:
    """Return the concatenation of two strings."""
    return "{}{}".format(str1, str2)
