#!usr/bin/python3
# -*- coding: utf-8 -*-

import asyncio

async def foo():
    print('Enter foo')
    await asyncio.sleep(1)
    print('End foo')


async def bar():
    print('Enter bar')
    await foo()
    print('End bar')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bar())
    loop.close()
