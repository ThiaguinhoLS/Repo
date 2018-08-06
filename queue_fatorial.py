#!usr/bin/python3
# -*- coding: utf-8 -*-

from queue import Queue
from threading import Thread


def fatorial(x):
    'Cálculo de fatorial'
    if x < 2:
        return 1
    return x * fatorial(x - 1)


def worker(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(fatorial(item))
        q.task_done()


if __name__ == '__main__':
    q = Queue(maxsize=0)
    threads = []
    for _ in range(2):
        t = Thread(target=worker, args=(q,))
        t.start()
        threads.append(t)
    for i in range(10):
        q.put(i)
    q.put(None)
    for t in threads:
        t.join()
