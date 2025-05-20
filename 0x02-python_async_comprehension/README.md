# 0x02-python_async_comprehension

This directory contains Python files exploring asynchronous generators and comprehensions.

## Files:

- `0-async_generator.py`: Contains an async generator that yields random numbers with delays.
- `1-async_comprehension.py`: Contains an async comprehension that collects random numbers from the generator.
- `2-measure_runtime.py`: Contains a coroutine that measures the runtime of parallel async comprehensions.

## Runtime Explanation

The total runtime in `2-measure_runtime.py` is roughly 10 seconds because:
1. Each `async_comprehension()` call takes 10 seconds (1 second per number × 10 numbers)
2. When running four comprehensions in parallel using `asyncio.gather()`, they all execute concurrently
3. Since they're running in parallel, the total runtime is determined by the longest-running task
4. Therefore, the total runtime is approximately 10 seconds, not 40 seconds (which would be the case if they ran sequentially) 