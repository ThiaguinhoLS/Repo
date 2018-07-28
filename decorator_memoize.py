#!usr/bin/python3
# -*- coding: utf-8 -*-
from functools import wraps


def decorator(func):

    _cache = {}

    @wraps(func)
    def _wrapper(*args, **kwargs):
        key = args + tuple(kwargs.items())
        if key not in _cache:
            _cache[key] = func(*args, **kwargs)
        return _cache[key]

    return _wrapper


@decorator
def fat(number):
    value = 1
    for i in range(1, number + 1):
        value *= i
    return value
