# -*- coding: utf-8 -*-
from functools import wraps


def decorator(func):
    @wraps(func)
    def _wrapper(message):
        print('{:*^30}'.format('Mensagem'))
        func(message)
    return _wrapper


@decorator
def show_message(message):
    print(message)


if __name__ == '__main__':
    show_message('hello world')
