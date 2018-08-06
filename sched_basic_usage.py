#!usr/bin/python3
# -*- coding: utf-8 -*-

import sched
import time


def task(argument='default'):
    print('Execute {} in {}'.format(argument, time.ctime()))


if __name__ == '__main__':
    scheduler = sched.scheduler()
    scheduler.enter(delay=1, priority=1, action=task, argument=('positional',))
    scheduler.enter(
        delay=.99,
        priority=0,
        action=task,
        kwargs={'argument': 'keyword'}
    )
    print('Initialize in:', time.ctime())
    scheduler.run(blocking=True)
