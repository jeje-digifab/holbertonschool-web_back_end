#!/usr/bin/env python3
"""
This script defines an asynchronous coroutine that waits for a random delay.
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time_async(n: int, max_delay: int) -> float:
    """
    Asynchronously measure the total execution time for wait_n(n, max_delay).

    Args:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay for each call to wait_n.

    Returns:
        float: The average time per call to wait_n.
    """
    start_time: float = time.time()
    await wait_n(n, max_delay)
    end_time: float = time.time()
    total_time: float = end_time - start_time
    return total_time / n


def measure_time(n: int, max_delay: int) -> float:
    """
    Synchronously measure the total execution time for wait_n(n, max_delay).

    Args:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay for each call to wait_n.

    Returns:
        float: The average time per call to wait_n.
    """
    return asyncio.run(measure_time_async(n, max_delay))
