#!usr/bin/python3
# -*- coding: utf-8 -*-


def minimize():
    current = yield
    while True:
        value = yield current
        current = min(value, current)


if __name__ == '__main__':
    r = minimize()
    next(r)
    print(r.send(10))
    print(r.send(5))
    print(r.send(11))
    print(r.send(-1))
