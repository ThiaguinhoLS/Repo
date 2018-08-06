#!usr/bin/python3
# -*- coding: utf-8 -*-

from concurrent.futures import ThreadPoolExecutor
import threading


def task():
    print('Executando a task')
    result = 0
    for i in range(10):
        result += i
    print('Resultado:', result)
    print('Task executada {}'.format(threading.current_thread()))


def main():
    executor = ThreadPoolExecutor(max_workers=2)
    executor.submit(task)
    executor.submit(task)


if __name__ == '__main__':
    main()
