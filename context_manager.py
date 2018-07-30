#!usr/bin/python3
# -*- coding: utf-8 -*-

from functools import partial

class FileOpener(object):

    def __init__(self, filename, mode='w'):
        self._opener = partial(open, filename, mode=mode)

    def __enter__(self):
        self.file = self._opener()
        return self.file

    def __exit__(self, *exc_args):
        self.file.close()


with FileOpener('blah.txt') as f:
    f.write('blah blah ...')
