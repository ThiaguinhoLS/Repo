# -*- coding: utf-8 -*-
from functools import lru_cache
from time import time


def fat(x): # Time: 0.00006676
        value = 1
        for i in range(1, x + 1):
            value *= i
        return value


@lru_cache(maxsize=None)
def fat_cache(x):
        value = 1
        for i in range(1, x + 1):
            value *= i
        return value


def main():
    funcs = (fat, fat_cache)
    for func in funcs:
        start = time()
        for value in (10, 20, 30):
            print(func(value))
    print('Time: {}'.format(time() - start))
