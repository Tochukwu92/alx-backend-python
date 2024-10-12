#!/usr/bin/env python3

'''takes in a string and int or float and return result'''


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    to_kv - takes in a string and number and return tuple
    '''
    output: Tuple[str, float] = (k, v * v)
    return output
