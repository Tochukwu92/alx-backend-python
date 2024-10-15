#!/usr/bin/env python3

'''async function that genarate a random number'''


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    generate a random number and delay for a perticular seconds
    '''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
