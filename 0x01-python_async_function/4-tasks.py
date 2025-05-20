import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times and returns a list of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = []
    for task in asyncio.as_completed(tasks):
        result = await task
        results.append(result)
    # Similar to wait_n, as_completed is used. If sorted output is strictly required
    # and tests fail, sorting might be necessary despite the prompt.
    return results 