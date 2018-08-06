#!usr/bin/python3
# -*- coding: utf-8 -*-

import asyncio


async def first_coro():
    while True:
        await asyncio.sleep(3)
        print('Primeira corotina executada')


async def second_coro():
    while True:
        await asyncio.sleep(3)
        print('Segunda corotina executada')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        asyncio.ensure_future(first_coro())
        asyncio.ensure_future(second_coro())
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
