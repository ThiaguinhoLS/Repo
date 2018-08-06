#!usr/bin/python
# -*- coding: utf-8 -*-

import threading
import queue


class ThreadClass(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._queue = queue
        print('Instanciada a thread:', self.getName())

    def run(self):
        print('Iniciando a thread:', self.getName())
        while True:
            item = self._queue.get()
            print(item)
            if item is None:
                break
            double(item)
        print('Finalizando a thread:', self.getName())


def double(value):
    return value * 2

q = queue.Queue(maxsize=0)


# Inicia as threads
threads = []
for _ in range(2):
    t = ThreadClass(q)
    t.setDaemon(True)
    t.start()
    threads.append(t)

# Insere items na queue
for i in range(100):
    q.put(i)

for i in range(2):
    q.put(None)


q.join()
for t in threads:
    print('t')
    t.join()
print('olá')
