# -*- coding: utf-8 -*-
from functools import wraps


def decorator(func):
    @wraps(func)
    def _wrapper(message):
        func(message)
    return _wrapper

@decorator
def show_message(message):
    print(message)



