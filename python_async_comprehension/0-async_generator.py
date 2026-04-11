#!/usr/bin/env python3
"""Async Generator"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Async Generator that yields a random number between 0 and 10
    after a random delay between 0 and 10 seconds."""
    for _ in range(10):
        await asyncio.sleep(random.uniform(0, 10))
        yield random.uniform(0, 10)
