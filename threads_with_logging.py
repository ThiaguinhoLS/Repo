#!usr/bin/python3
# -*- coding: utf-8 -*-

import threading
import logging
import time


def worker():
    logging.debug(
        'Iniciando worker, thread name: {}'.format(
            threading.current_thread().getName()
        )
    )
    time.sleep(1)
    logging.debug(
        'Encerrando worker, thread name: {}'.format(
            threading.current_thread().getName()
        )
    )


def other_worker():
    logging.debug(
        'Iniciando other_worker, thread name: {}'.format(
            threading.current_thread().getName()
        )
    )
    time.sleep(2)
    logging.debug(
        'Encerrando other_worker, thread name: {}'.format(
            threading.current_thread().getName()
        )
    )


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(levelname)s]:%(message)s',
    )
    thread_one = threading.Thread(target=worker, name='worker', daemon=True)
    thread_two = threading.Thread(
        target=other_worker,
        name='other_worker',
        daemon=True
    )
    thread_three = threading.Thread(target=worker, daemon=True)
    thread_one.start()
    thread_two.start()
    thread_three.start()
    thread_one.join()
    thread_two.join()
    thread_three.join()
