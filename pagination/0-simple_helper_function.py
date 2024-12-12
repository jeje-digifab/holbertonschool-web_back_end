#!/usr/bin/env python3
"""
This script calculate the start and end indexes for pagination.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for pagination.

    This function takes a page number and a page size, and returns a tuple
    containing the start index and end index for the specified page.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple[int, int]: A tuple containing the start index and end index.
    """
    start_index: int = (page - 1) * page_size
    end_index: int = page_size + start_index
    return start_index, end_index
