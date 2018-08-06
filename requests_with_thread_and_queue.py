#!usr/bin/python3
# -*- coding: utf-8 -*-

from queue import Queue
from threading import Thread
import requests


def fetch(q):
    while not q.empty():
        url = q.get()
        content = request.get(url).json()['sprites']
        q.task_done()
