#!/usr/bin/env python3
"""
This script defines an asynchronous coroutine that waits for a random delay.
"""

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    Waits for a random delay `n` times and returns a sorted list of delays.

    :param n: Number of times to wait.
    :param max_delay: Maximum delay for each wait.
    :return: Sorted list of delays.
    """
    x = 0
    delays: list[float] = []
    while x < n:
        delays.append(await wait_random(max_delay))
        x += 1
    return sorted(delays)
