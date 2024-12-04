#!/usr/bin/env python3
"""
This script defines an asynchronous coroutine that waits for a random delay.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    Waits for a random delay `n` times and returns a sorted list of delays.

    :param n: Number of times to wait.
    :param max_delay: Maximum delay for each wait.
    :return: Sorted list of delays.
    """
    delays: list[float] = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
