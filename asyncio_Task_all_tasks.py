#!usr/bin/python3
# -*- coding: utf-8 -*-

import asyncio
import time


async def coro():
    time.sleep(1)
    print('Task processada')


async def main():
    for _ in range(5):
        asyncio.ensure_future(coro())
    pending = asyncio.Task.all_tasks()
    print(pending)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
        print('Tasks completas')
    finally:
        loop.close()
