#!/usr/bin/env python3

"""returns a callable function"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    takes in a float and return a function
    '''
    def multiplier_func(x: float) -> float:
        '''
        takes in a float and return a float
        '''
        return x * multiplier
    return multiplier_func
