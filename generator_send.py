#!usr/bin/python3
# -*- coding: utf-8 -*-


def coroutine():
    while True:
        received = yield
        print('Received:', received)


if __name__ == '__main__':
    r = coroutine()
    next(r)
    r.send('First')
    r.send('Second')
