#!usr/bin/python3
# -*- coding: utf-8 -*-

#from multiprocessing import Pool
from multiprocessing.dummy import Pool
from os import getpid
from pprint import pprint
from requests import get
from contextlib import contextmanager
from time import time


def double(number):
    return number * 2, getpid()


def fetch(url):
    return get(url).status_code, getpid()


workers = Pool(6)


urls = [
    'http://google.com',
    'http://yahoo.com',
    'http://youtube.com',
    'http://facebook.com',
    'http://twitter.com',
    'http://instagram.com'
]


@contextmanager
def timeit():
    start = time()
    yield
    print('Tempo decorrido:', time() - start)


if __name__ == '__main__':
    with timeit():
        results = workers.map(fetch, urls)
        pprint(results)

