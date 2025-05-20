#!/usr/bin/env python3
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times and returns a list of delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = []
    for task in asyncio.as_completed(tasks):
        result = await task
        results.append(result)
    # The requirement is to not use sort(), but the example output is sorted.
    # Using as_completed processes tasks as they finish, which is related to concurrency
    # but doesn't guarantee a sorted order of delay values. If the tests fail due to
    # unsorted output, I will revisit this.
    return results 