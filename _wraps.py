# -*- coding: utf-8 -*-


def _wraps(func):
    def _wrapper(deco):
        deco.__name__ = func.__name__
        deco.__doc__ = func.__doc__
        return deco
    return _wrapper


def decorator(func):
    @_wraps(func)
    def _wrapper(message):
        func(message)
    return _wrapper


@decorator
def show_message(message):
    print(message)


class _wraps(object):

    def __init__(self, func):
        pass
