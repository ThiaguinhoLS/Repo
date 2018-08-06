#!usr/bin/python3
# -*- coding: utf-8 -*-

import threading
import time
import queue
import requests


class Consumer(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        while True:
            print(self._queue.queue)
            content = self._queue.get()
            if isinstance(content, str) and content == 'quit':
                break
            response = requests.get(content)
        print('Finalizando')



def Producer():
    urls = [
        'http://www.google.com', 'http://www.yahoo.com',
        'http://www.scala.org', 'http://www.python.org'
    ]
    q = queue.Queue(maxsize=0)
    worker_threads = build_worker_pool(q, 4)
    start_time = time.time()

    for url in urls:
        q.put(url)
    for worker in worker_threads:
        q.put('quit')
    for worker in worker_threads:
        print(worker.getName())
        worker.join()

    print('Terminou com o tempo:', time.time() - start_time)


def build_worker_pool(q, size):
    workers = []
    for _ in range(size):
        worker = Consumer(q)
        worker.start()
        workers.append(worker)
    return workers


if __name__ == '__main__':
    Producer()
