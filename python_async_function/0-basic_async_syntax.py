#!/usr/bin/env python3
"""Basic async coroutine module"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Return a random float delay after waiting asynchronously."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
