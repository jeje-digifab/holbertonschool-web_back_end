### Task Summary for README

#### 0. Async Generator
**Mandatory**
- **Task**: Write a coroutine called `async_generator` that takes no arguments.
- **Details**: The coroutine will loop 10 times, each time asynchronously waiting for 1 second, then yielding a random number between 0 and 10 using the `random` module.
- **File**: `0-async_generator.py`
- **Directory**: `python_async_comprehension`
- **Repository**: `holbertonschool-web_back_end`

#### 1. Async Comprehensions
**Mandatory**
- **Task**: Import `async_generator` from the previous task and write a coroutine called `async_comprehension` that takes no arguments.
- **Details**: The coroutine will collect 10 random numbers using an async comprehension over `async_generator`, then return the 10 random numbers.
- **File**: `1-async_comprehension.py`
- **Directory**: `python_async_comprehension`
- **Repository**: `holbertonschool-web_back_end`

#### 2. Run time for four parallel comprehensions
**Mandatory**
- **Task**: Import `async_comprehension` from the previous file and write a `measure_runtime` coroutine that will execute `async_comprehension` four times in parallel using `asyncio.gather`.
- **Details**: `measure_runtime` should measure the total runtime and return it. The total runtime is roughly 10 seconds.
- **File**: `2-measure_runtime.py`
- **Directory**: `python_async_comprehension`
- **Repository**: `holbertonschool-web_back_end`
