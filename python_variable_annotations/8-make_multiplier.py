#!/usr/bin/env python3
"""
This script performs various operations, such as converting floats to strings,
flooring values, and concatenating strings.

It is designed to be executed with Python 3.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a number by a given multiplier.

    Args:
        multiplier (float): The multiplier to use for the multiplication.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the product of that float and the multiplier.
    """
    return lambda x: x * multiplier
