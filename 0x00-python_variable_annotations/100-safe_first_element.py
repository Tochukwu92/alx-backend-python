#!/usr/bin/env python3

'''annotating to duck-typed'''


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    safe_first_element - duck-typed annotation
    '''
    if lst:
        return lst[0]
    else:
        return None
