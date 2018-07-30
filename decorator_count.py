#!usr/bin/python3
# -*- coding: utf-8 -*-

from functools import wraps


def deco_counter(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0    
    return wrapper


@deco_counter
def double(x):
    return x * 2


