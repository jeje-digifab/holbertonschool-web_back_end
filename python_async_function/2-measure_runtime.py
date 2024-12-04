#!/usr/bin/env python3
"""
This script defines an asynchronous coroutine that waits for a random delay.
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def _measure_time(n: int, max_delay: int) -> float:
    start_time: float = time.time()
    await wait_n(n, max_delay)
    end_time: float = time.time()
    total_time: float = end_time - start_time
    return total_time / n


def measure_time(n: int, max_delay: int) -> float:
    return asyncio.run(_measure_time(n, max_delay))
