### Tasks Overview

#### 0. Simple Helper Function
- **Mandatory**
- **Description**: Write a function named `index_range` that takes two integer arguments: `page` and `page_size`. The function should return a tuple containing the start and end indexes corresponding to the range of indexes to return in a list for those pagination parameters. Page numbers are 1-indexed.
- **Example**:
  ```python
  res = index_range(1, 7)
  print(res)  # Output: (0, 7)
  ```
- **File**: `0-simple_helper_function.py`

#### 1. Simple Pagination
- **Mandatory**
- **Description**: Implement a method named `get_page` in the `Server` class that takes two integer arguments: `page` (default 1) and `page_size` (default 10). The method should use the `index_range` function to paginate a dataset of popular baby names from a CSV file and return the appropriate page of the dataset.
- **Requirements**:
  - Use assertions to verify that both arguments are integers greater than 0.
  - Return an empty list if the input arguments are out of range for the dataset.
- **File**: `1-simple_pagination.py`

#### 2. Hypermedia Pagination
- **Mandatory**
- **Description**: Implement a method named `get_hyper` in the `Server` class that takes the same arguments as `get_page` and returns a dictionary containing the following key-value pairs:
  - `page_size`: the length of the returned dataset page
  - `page`: the current page number
  - `data`: the dataset page
  - `next_page`: number of the next page, `None` if no next page
  - `prev_page`: number of the previous page, `None` if no previous page
  - `total_pages`: the total number of pages in the dataset
- **File**: `2-hypermedia_pagination.py`

#### 3. Deletion-Resilient Hypermedia Pagination
- **Mandatory**
- **Description**: Implement a method named `get_hyper_index` in the `Server` class that takes two integer arguments: `index` (default `None`) and `page_size` (default 10). The method should return a dictionary with the following key-value pairs:
  - `index`: the current start index of the return page
  - `next_index`: the next index to query with
  - `page_size`: the current page size
  - `data`: the actual page of the dataset
- **Requirements**:
  - Use assertions to verify that `index` is in a valid range.
  - Ensure that the user does not miss items from the dataset when changing pages, even if certain rows are removed between queries.
- **File**: `3-hypermedia_del_pagination.py`
