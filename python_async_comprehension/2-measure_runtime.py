#!/usr/bin/env python3
"""
This script defines an asynchronous generator that waits for a random delay.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing the async_comprehension coroutine
        four times in parallel.

    This function creates a list of four async_comprehension coroutines
        and uses asyncio.gather to execute them in parallel.
    It measures the time before and after the execution of these coroutines
        and returns the total runtime.

    Returns:
        float: The total runtime in seconds.
    """
    start_time: float = time.time()

    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)

    end_time: float = time.time()
    total_time: float = end_time - start_time
    return total_time
