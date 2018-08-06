#!usr/bin/python3
# -*- coding: utf-8 -*-

from multiprocessing.dummy import Pool as ThreadPool
import requests
from contextlib import contextmanager
from time import time


urls = [
  'http://www.python.org', 
  'http://www.python.org/about/',
  'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
  'http://www.python.org/doc/',
  'http://www.python.org/download/',
  'http://www.python.org/getit/',
  'http://www.python.org/community/',
  'https://wiki.python.org/moin/',
]

@contextmanager
def timeit():
	start = time()
	yield
	print('Tempo decorrido: ', time() - start)


if __name__ == '__main__':
	with timeit():
		pool = ThreadPool(3)
		results = pool.map(requests.get, urls)
		pool.close()
		pool.join()
	# Uma thread: Tempo decorrido:  7.978792428970337
	# Duas threads: Tempo decorrido:  5.130387306213379
	# Três threads: Tempo decorrido:  3.6528573036193848 