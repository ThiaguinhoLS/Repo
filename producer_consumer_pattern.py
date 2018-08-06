#!usr/bin/python3
# -*- coding: utf-8 -*-

import time
import threading
import queue


class Consumer(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        while True:
            message = self._queue.get()
            if isinstance(message, str) and message == 'quit':
                break
            print('Recebi a mensagem', message)
        print('Finalizou a thread')


def producer():
    q = queue.Queue(maxsize=0)
    worker = Consumer(q)
    worker.start()
    start_time = time.time()
    while time.time() - start_time < 5:
        q.put('Hello world em {}'.format(time.time()))
        time.sleep(1)
    q.put('quit')
    worker.join()


if __name__ == '__main__':
    producer()
