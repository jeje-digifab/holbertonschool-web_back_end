#!/usr/bin/env python3
"""
This script defines an asynchronous coroutine that waits for a random delay.
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Coroutine that waits for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int): The maximum delay in seconds. Default is 10.

    Returns:
        float: The actual delay waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
