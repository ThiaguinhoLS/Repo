#!usr/bin/python3
# -*- coding: utf-8 -*-

from multiprocessing import Process
from pickle import dumps


def decorator(func):
    def wrapper():
        pass
    return wrapper

@decorator
def blah(x, y):
    return x, y


print(dumps(blah))
print(dumps(decorator)) # Não consegue serializar closures
