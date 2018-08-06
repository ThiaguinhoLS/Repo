#!usr/bin/python3
# -*- coding: utf-8 -*-

import threading
import datetime


class ThreadClass(threading.Thread):

    def run(self):
        now = datetime.datetime.now()
        print('{} diz hello world em: {}'.format(self.getName(), now))


for _ in range(2):
    t = ThreadClass()
    t.start()
