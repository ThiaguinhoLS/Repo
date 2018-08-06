#!usr/bin/python3
# -*- coding: utf-8 -*-

from concurrent.futures import ThreadPoolExecutor


def task(name):
    print('Thread atual é:', name)


def main():
    print('Iniciando a execução')
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.submit(task, 'task1')
        executor.submit(task, 'task2')
        executor.submit(task, 'task3')
    print('Terminou a execução')


if __name__ == '__main__':
    main()
