#!usr/bin/python3
# -*- coding: utf-8 -*-

from functools import wraps, partial


def decorator(message):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(message, end=' ')
            return func(*args, **kwargs)
        return wrapper
    return deco


def decorator(message, func=None):
    if func is None:
        return lambda func: decorator(message, func)
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(message, end=' ')
        return func(*args, **kwargs)
    return wrapper


def decorator(message, func=None):
    if func is None:
        return partial(decorator, message)
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(message, end=' ')
        return func(*args, **kwargs)
    return wrapper


@decorator('O dobro é:')
def double(number):
    return number * 2


