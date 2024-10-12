#!/usr/bin/env python3


'''typed annotation'''


from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')  # Declare a generic type variable


def safely_get_value(
    dct: Mapping[
        Any, T], key: Any, default: Union[
            T, None] = None) -> Union[T, None]:
    if key in dct:
        return dct[key]
    else:
        return default
