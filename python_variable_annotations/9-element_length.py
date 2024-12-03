#!/usr/bin/env python3
"""
This script performs various operations, such as converting floats to strings,
flooring values, and concatenating strings.

It is designed to be executed with Python 3.
"""

from typing import Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> Iterable[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, where each tuple contains an element from
    the input list and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences
        (e.g., strings, lists, tuples).

    Returns:
        Iterable[Tuple[Sequence, int]]: An iterable of tuples, where each
        tuple contains an element from the input list and its length.
    """

    return [(i, len(i)) for i in lst]
