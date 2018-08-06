#!usr/bin/python3
# -*- coding: utf-8 -*-

import queue

q = queue.Queue(maxsize=0)

for i in range(5):
    q.put(i)


while not q.empty():
    print(q.get())
