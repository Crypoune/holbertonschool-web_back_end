#!/usr/bin/env python3
"""Measure runtime of async execution"""
import asyncio
import time
import importlib

wait_n = importlib.import_module('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Return average runtime per coroutine."""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start) / n
