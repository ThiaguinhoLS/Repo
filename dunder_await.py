#!usr/bin/python3
# -*- coding: utf-8 -*-

from collections.abc import Awaitable
from random import randint
import asyncio


class AsynchronousRandom(Awaitable):

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __await__(self):
        return self.randint(self.start, self.stop).__await__()

    async def randint(self, start, stop):
        value = randint(start, stop)
        return await asyncio.sleep(1, result=value)


async def main():
    while True:
        random = AsynchronousRandom(1, 10)
        print(await random)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
