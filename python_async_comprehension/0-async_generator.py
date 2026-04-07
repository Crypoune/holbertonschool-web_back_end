#!/usr/bin/env python3
"""Async Generator"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yield 10 random floats asynchronously, waiting 1 second between each yield."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
