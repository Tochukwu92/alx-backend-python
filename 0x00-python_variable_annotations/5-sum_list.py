#!/usr/bin/env python3

'''sum up elements inside a list'''


from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
    sum_list - sum elements in a list and return flaot
    '''
    total: float = 0
    for i in range(len(input_list)):
        total += input_list[i]
    return total
