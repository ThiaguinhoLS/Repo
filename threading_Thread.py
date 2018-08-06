#!usr/bin/python3
# -*- coding: utf-8 -*-

from threading import Thread


def hello(name):
    print('Hello World')


if __name__ == '__main__':
    thread = Thread(
        target=hello,
        name='Minha thread',
        args=('Thiago',),
        daemon=True
    )
    thread.start()
