### Tasks Summary for README

#### 0. The basics of async
- **Description**: Write an asynchronous coroutine `wait_random` that takes an integer argument `max_delay` (default value of 10). The coroutine waits for a random delay between 0 and `max_delay` (inclusive, float value) seconds and returns the delay.
- **File**: `0-basic_async_syntax.py`
- **Directory**: `python_async_function`
- **Repository**: `holbertonschool-web_back_end`

#### 1. Let's execute multiple coroutines at the same time with async
- **Description**: Import `wait_random` from the previous file and write an async routine `wait_n` that takes two integer arguments: `n` and `max_delay`. Spawn `wait_random` `n` times with the specified `max_delay` and return the list of all delays in ascending order without using `sort()`.
- **File**: `1-concurrent_coroutines.py`
- **Directory**: `python_async_function`
- **Repository**: `holbertonschool-web_back_end`

#### 2. Measure the runtime
- **Description**: Import `wait_n` from the previous file and create a `measure_time` function that takes integers `n` and `max_delay` as arguments. Measure the total execution time for `wait_n(n, max_delay)` and return `total_time / n`. Use the `time` module to measure the elapsed time.
- **File**: `2-measure_runtime.py`
- **Directory**: `python_async_function`
- **Repository**: `holbertonschool-web_back_end`

#### 3. Tasks
- **Description**: Import `wait_random` from `0-basic_async_syntax` and write a function `task_wait_random` that takes an integer `max_delay` and returns an `asyncio.Task`.
- **File**: `3-tasks.py`
- **Directory**: `python_async_function`
- **Repository**: `holbertonschool-web_back_end`

#### 4. Tasks
- **Description**: Modify the `wait_n` function to create a new function `task_wait_n`. The new function should call `task_wait_random` instead of `wait_random`.
- **File**: `4-tasks.py`
- **Directory**: `python_async_function`
- **Repository**: `holbertonschool-web_back_end`

This summary provides an overview of the tasks and their corresponding files, directories, and repository for the README.
