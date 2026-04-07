#!/usr/bin/env python3
"""Module for concurrent coroutines."""
import asyncio
import importlib
from typing import List

wait_random = importlib.import_module('0-basic_async_function').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times and return delays in ascending order."""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
