#!usr/bin/python3
# -*- coding: utf-8 -*-

import time


def double(number):
    print('Dobro:', number * 2)


def generate_pairs(limit):
    for i in range(limit):
        print('enter')
        yield i
        print('exit')


def main():
    gen = generate_pairs(10)
    while True:
        time.sleep(0.05)
        value = next(gen)
        print(value)
        if value % 2 == 0:
            double(value)
        time.sleep(0.05)


main()
