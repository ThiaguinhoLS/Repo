#!usr/bin/python3
# -*- coding: utf-8 -*-

from requests import get
from queue import Queue
from threading import Thread
from time import time





class ThreadClass(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self._queue = queue

    def run(self):
        while True:
            url = self._queue.get(block=True, timeout=None) # Argumentos padrão
            response = get(url, stream=True)
            print(response.content)
            print(content)
            self._queue.task_done()


q = Queue(maxsize=0)
start = time()
urls = [
    'http://google.com',
    'http://yahoo.com',
    'http://youtube.com'
]


def main():
    for i in range(5):
        t = ThreadClass(q)
        t.setDaemon(True)
        t.start()

    for url in urls:
        q.put(url)



main()
print('Terminou em:', time() - start)
q.join()
        
