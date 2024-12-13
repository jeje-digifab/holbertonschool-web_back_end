#!/usr/bin/env python3
"""
This script calculate the start and end indexes for pagination.
"""
import csv
import math
from re import A
from typing import List, Tuple, Dict, Any, Optional


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a specific page of data from a CSV file.

        This function reads data from a CSV file named 'Popular_Baby_Names.csv'
            and returns a subset of the data
        corresponding to the specified page and page size.

        Args:
            page (int): The page number to retrieve.
            Must be an integergreater than 0. Default is 1.

            page_size (int): The number of rows per page.
            Must be an integer greater than 0. Default is 10.

        Returns:
            List[List]: A list of rows from the CSV file corresponding
                            to the specified page.
                        Returns an empty list if the start index is out
                            of the range of the data.

        Raises:
            AssertionError: If `page` or `page_size` is not an integer
                greater than 0.
        """
        assert isinstance(
            page, int) and page > 0, "Page must be an integer greater than 0"

        assert (
            isinstance(page_size, int) and page_size > 0
        ), "Page size must be an integer greater than 0"

        data = self.dataset()

        start_index, end_index = index_range(page, page_size)

        if start_index >= len(data):
            return []
        return data[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Retrieves a specific page of data with hypermedia information.

        This function retrieves a specific page of data from the dataset and
        includes hypermedia information such as the current page, page size,
        next page, previous page, and total number of pages.

        Args:
            page (int): The page number to retrieve.
            Must be an integer greater than 0. Default is 1.

            page_size (int): The number of rows per page.
            Must be an integer greater than 0. Default is 10.

        Returns:
            Dict[str, Any]: A dictionary containing the following keys:
                - "page_size" (int): The number of items per page.
                - "page" (int): The current page number.
                - "data" (List[List[Any]]): The list of rows for
                    the specified page.
                - "next_page" (Optional[int]): The next page number
                    if available, otherwise None.
                - "prev_page" (Optional[int]): The previous page number
                    if available, otherwise None.
                - "total_pages" (int): The total number of pages.

        Raises:
            AssertionError: If `page` or `page_size` is not an integer
            greater than 0.
        """
        page_data: List[List[Any]] = self.get_page(page, page_size)
        return {
            "page_size": page_size,
            "page": page,
            "data": page_data,
            "next_page": page + 1 if len(page_data) == page_size else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": math.ceil(len(self.dataset()) / page_size)
        }


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
