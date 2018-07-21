# -*- coding: utf-8 -*-
class Immutable(tuple):

    def __new__(cls, a, b):
	return tuple.__new__(cls, (a, b))

    def __getattr__(self, attrname):
	if attrname == 'a':
            return self[0]
        elif attrname == 'b':
    	    return self[1]
        raise AttributeError(f'{attrname} is not defined')

    def __setattr__(self, attrname, value):
	raise TypeError('{__class__.__name__} is immutable')



from collections import namedtuple

class Immutable(namedtuple('Immutable', ['a', 'b'])):

    __slots__ = ()

