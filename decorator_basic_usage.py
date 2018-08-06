#!usr/bin/python3
# -*- coding: utf-8 -*-

from functools import wraps

def deco_positive(func):
    @wraps(func)
    def wrapper(number):
        if number < 0:
            number = abs(number)
        return func(number)
    return wrapper


def show_number(number):
    print('Número é:', number)


show_number = deco_positive(show_number)
