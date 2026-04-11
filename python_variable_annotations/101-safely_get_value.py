#!/usr/bin/env python3
"""Function safely_get_value with generics"""
from typing import Any, TypeVar, Mapping, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Return the value from a mapping for a key, or a default."""
    if key in dct:
        return dct[key]
    else:
        return default
