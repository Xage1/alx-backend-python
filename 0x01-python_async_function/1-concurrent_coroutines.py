#!/usr/bin/env python3
""" Coroutine at the same time witha sync """
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Coroutine that spawns `n` `wait_random` coroutines with a specified
    `max_delay` and returns the list of delays in ascending order."""
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)

    sorted_results = sorted(results)

    return sorted_results
