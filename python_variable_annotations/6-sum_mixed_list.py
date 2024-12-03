#!/usr/bin/env python3
"""
This script performs various operations, such as converting floats to strings,
flooring values, and concatenating strings.

It is designed to be executed with Python 3.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a list of mixed integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing integers
        and floats.

    Returns:
        float: The sum of the list elements.
    """
    return sum(mxd_lst)
