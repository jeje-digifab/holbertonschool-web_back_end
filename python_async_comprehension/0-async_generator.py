#!/usr/bin/env python3
"""
This script defines an asynchronous generator that waits for a random delay.
"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    An asynchronous generator that yields random float values between 0 and 10.

    This generator waits for 1 second between each yield and generates a total
        of 10 values.

    Yields:
        float: A random float value between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        delay = random.uniform(0, 10)
        yield delay
