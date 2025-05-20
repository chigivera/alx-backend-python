# 0x01-python_async_function

This directory contains Python files exploring asynchronous programming with asyncio.

## Files:

- `0-basic_async_syntax.py`: Contains the `wait_random` coroutine that waits for a random delay.
- `1-concurrent_coroutines.py`: Contains the `wait_n` async function that runs `wait_random` multiple times concurrently.
- `2-measure_runtime.py`: Contains the `measure_time` function to measure the execution time of `wait_n`.
- `3-tasks.py`: Contains the `task_wait_random` function that creates an asyncio.Task for `wait_random`.
- `4-tasks.py`: Contains the `task_wait_n` async function that runs `task_wait_random` multiple times concurrently. 