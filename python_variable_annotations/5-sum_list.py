#!/usr/bin/env python3
"""
This script performs various operations, such as converting floats to strings,
flooring values, and concatenating strings.

It is designed to be executed with Python 3.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums all elements in the provided list of floating-point numbers.

    Args:
        input_list (List[float]): A list of floating-point numbers to sum.

    Returns:
        float: The sum of all the elements in the list.
    """
    return sum(input_list)
