#!usr/bin/python3
# -*- coding: utf-8 -*-

from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from contextlib import contextmanager
from requests import get
import time


@contextmanager
def timeit():
    start_time = time.time()
    yield
    print('Encerrado em:', time.time() - start_time)


urls = [
  'http://www.python.org', 
  'http://www.python.org/about/',
  'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
  'http://www.python.org/doc/',
  'http://www.python.org/download/',
  'http://www.python.org/getit/',
  'http://www.python.org/community/',
  'https://wiki.python.org/moin/',
  'http://planet.python.org/',
  'https://wiki.python.org/moin/LocalUserGroups',
  'http://www.python.org/psf/',
  'http://docs.python.org/devguide/',
  'http://www.python.org/community/awards/'
]


if __name__ == '__main__':
    with timeit():
        pool = ThreadPool(4)
        results = pool.map(get, urls)
        pool.close()
    pool.join()
