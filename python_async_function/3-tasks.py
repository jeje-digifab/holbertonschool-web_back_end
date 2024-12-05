#!/usr/bin/env python3
"""
This script defines an asynchronous coroutine that waits for a random delay.
"""

import asyncio
from typing import Any

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio Task that waits for a random delay.

    This function creates an asyncio Task that will wait for a random
    delay between 0 and `max_delay` seconds (inclusive).

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: The created asyncio Task.
    """
    coroutine = wait_random(max_delay)

    my_task = asyncio.create_task(coroutine)

    return my_task
