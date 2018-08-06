#!usr/bin/python3
# -*- coding: utf-8 -*-

import asyncio

async def coro():
    print('Hello world')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        result = loop.run_until_complete(coro())
    finally:
        loop.close()
