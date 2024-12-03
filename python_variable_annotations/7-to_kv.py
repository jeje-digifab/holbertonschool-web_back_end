#!/usr/bin/env python3
"""
This script performs various operations, such as converting floats to strings,
flooring values, and concatenating strings.

It is designed to be executed with Python 3.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple where the first element is the string `k`
    and the second element is the square of `v`.

    Parameters:
    k (str): A string that will be the first element of the returned tuple.
    v (Union[int, float]): An integer or float that will be squared and used
        as the second element of the returned tuple.

    Returns:
    Tuple[str, float]: A tuple containing the string `k` and the square of `v`.
    """
    return (k, v ** 2)
