#!usr/bin/python3
# -*- coding: utf-8 -*-

import asyncio
import time


async def coro():
    print('Iniciou a corotina')
    time.sleep(3)
    print('Finalizou a corotina')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(coro())
    finally:
        loop.close()
