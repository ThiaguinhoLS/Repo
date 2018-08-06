#!usr/bin/python3
# -*- coding: utf-8 -*-

from threading import Thread
import time


def func(name):
    print('Iniciado', name)
    time.sleep(5)
    print('Finalizado', name)


t = Thread(target=func, args=('Thread One',))
t.start()
print('Iniciou a thread')
t.join()
print('Terminou a thread')
