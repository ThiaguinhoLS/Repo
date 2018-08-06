#!usr/bin/python3
# -*- coding: utf-8 -*-

from collections import namedtuple
from multiprocessing import Process
from threading import Thread
from os import getpid, getppid


state = namedtuple('State', ['name', 'id', 'pid'])


def info(name):
    st = state(name, getpid(), getppid())
    print(st)


info('programa principal')
thread = Thread(target=info, args=('Thread',))
process = Process(target=info, args=('Process',))
thread.start()
process.start()
thread.join()
process.join()
