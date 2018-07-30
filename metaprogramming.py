#!usr/bin/python3
# -*- coding: utf-8 -*-


class Meta(type):

    def __new__(mcs, name, bases, dct):
        print(f'Classe instanciada {name}')
        klass = super().__new__(mcs, name, bases, dct)
        return klass


class Spam(metaclass=Meta):

    pass
