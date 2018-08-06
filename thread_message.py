#!usr/bin/python3
# -*- coding: utf-8 -*-

from threading import Thread
from queue import Queue

class ThreadClass(Thread):

    def __init__(self, queue):
        self._queue = queue
        Thread.__init__(self)

    def run(self):
        while True:
            message = self._queue.get()
            if message is None:
                break
            print(message)


def main():
    q = Queue(maxsize=0)
    thread = ThreadClass(q)
    thread.start()
    q.put('Bom dia')
    q.put('Boa noite')
    q.put(None)
    thread.join()


if __name__ == '__main__':
    main()
