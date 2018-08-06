#!usr/bin/python3
# -*- coding: utf-8 -*-

from queue import Queue
from threading import Thread


def do_stuff(q):
    while True:
        print(q.get())
        q.task_done()


if __name__ == '__main__':
    q = Queue(maxsize=0)
    for i in range(10):
        worker = Thread(target=do_stuff, args=(q,))
        worker.setDaemon(True)
        worker.start()
    for x in range(100):
        q.put(x)
    q.join()
