#!/usr/bin/env python3
"""Module for the task_wait_random function"""
import asyncio
import importlib

wait_random = importlib.import_module('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns an asyncio.Task that waits for a random delay and returns it"""
    return asyncio.create_task(wait_random(max_delay))
