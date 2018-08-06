#!usr/bin/python3
# -*- coding: utf-8 -*-

from threading import Thread, Event
from queue import Queue
from requests import get
import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

class Worker(Thread):

    def __init__(self, queue):
        super(Worker, self).__init__()
        self._queue = queue

    def run(self):
        event.wait()
        while not self._queue.empty():
            url = self._queue.get()
            response = get(url)
            logging.debug('{}: {}'.format(response.url, response.status_code))
            

if __name__ == '__main__':
    urls = [
        'http://google.com',
        'http://youtube.com',
    ]
    event = Event()
    queue = Queue(maxsize=2)
    worker = Worker(queue)
    worker.setDaemon(True)
    worker.start()
    for url in urls:
        queue.put(url)
    event.set()
    logging.info('Esperando finalização do worker')
    worker.join()
    logging.info('Finalizado o worker')
