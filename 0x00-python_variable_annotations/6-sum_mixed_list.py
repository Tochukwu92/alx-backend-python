#!/usr/bin/env python3

'''sum up elements in a list and return their sum'''


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    sum_mixed_list - sum elements in a list
    '''
    result: float = 0.0
    for i in range(len(mxd_lst)):
        result += mxd_lst[i]
    return result
