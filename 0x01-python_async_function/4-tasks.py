#!/usr/bin/env python3

'''Spawn task_wait_random n times with the specified max_delay'''
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with the specified max_delay and
    return the list of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task  # Await each task and get the result (the delay)
        delays.append(delay)

    return delays
