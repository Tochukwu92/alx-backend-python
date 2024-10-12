#!/usr/bin/env python3

'''takes in a list and return a list iterable'''


from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    element_length - retruns a list of tuple
    '''
    return [(i, len(i)) for i in lst]
