#!/usr/bin/env python3
"""
This script defines an asynchronous generator that waits for a random delay.
"""


from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    An asynchronous coroutine that collects 10 random float values using
        an async comprehension over async_generator.

    This coroutine iterates over the async_generator to collect 10 random
        float values between 0 and 10,
    with a 1-second delay between each value. The collected values are
        then returned as a list.

    Returns:
        List[float]: A list of 10 random float values.
    """
    delays: List[float] = []

    async for item in async_generator():
        delays.append(item)

    return delays
