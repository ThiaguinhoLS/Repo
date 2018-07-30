#!usr/bin/python3
# -*- coding: utf-8 -*-

def countdown(n):
    print('called')
    while n > 0:
        print('while')
        yield n
        n -= 1


if __name__ == '__main__':
    for i in countdown(10):
        print(i)
