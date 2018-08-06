#!usr/bin/python3
# -*- coding: utf-8 -*-

import threading
from time import sleep


def worker():
    print('Worker 1 iniciado')
    sleep(3)
    print('Worker 1 finalizado')


def worker_with_argument(number):
    print('Worker {} iniciado\n'.format(number))
    sleep(number)
    print('Worker {} finalizado'.format(number))


def worker_current_thread_name():
	print('Thread atual {}'.format(threading.current_thread().getName()))
	sleep(1)


thread_one = threading.Thread(target=worker, name='worker one')
thread_one.start()
thread_two = threading.Thread(target=worker_with_argument, args=(2,), name='worker two')
thread_two.start()
thread_one.join()
thread_two.join()
thread_three = threading.Thread(target=worker_current_thread_name, name='worker three')
thread_three.start()
thread_three.join()
