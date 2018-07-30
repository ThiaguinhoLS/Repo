#!usr/bin/python
# -*- coding: utf-8 -*-

import sched, time

def print_time(a='default'):
    print('From print_time', time.time(), a)


def print_some_times():
    print(time.time())
    scheduler.enter(delay=10, priority=1, action=print_time)
    scheduler.enter(delay=5, priority=2, action=print_time, argument=('positional',))
    scheduler.enter(delay=5, priority=1, action=print_time, kwargs={'a': 'keyword'})
    # Atributo somente leitura, retorna uma lista dos próximos eventos na ordem que serão executados
    print(scheduler.queue) 
    scheduler.run(blocking=False)
    print(time.time())


if __name__ == '__main__':
    scheduler = sched.scheduler(time.time, time.sleep)
    print_some_times()
