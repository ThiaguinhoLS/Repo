#!usr/bin/python
# -*- coding: utf-8 -*-


class A:
    
    def __init__(self):
        print('__init__ A')
        super().__init__()


class B(A):

    def __init__(self):
        print('__init__ B')
        super().__init__()

class C(A):

    def __init__(self):
        print('__init__ C')
        super().__init__()


class D(B):

    def __init__(self):
        print('__init__ D')
        super().__init__()


class E(C, D):

    def __init__(self):
        print('__init__ E')
        super().__init__()


if __name__ == '__main__':
    print(E.__mro__)
    # (<class '__main__.E'>,
    # <class '__main__.C'>,
    # <class '__main__.D'>,
    # <class '__main__.B'>,
    # <class '__main__.A'>,
    # <class 'object'>)
