#!usr/bin/python3
# -*- coding: utf-8 -*-

from collections.abc import AsyncIterator
import asyncio


class AsyncIter(AsyncIterator):

    def __init__(self, iterable, *, loop=None):
        self._iterator = iter(iterable)
        self.loop = loop or asyncio.get_event_loop()

    async def __anext__(self):
        value = await self.loop.run_in_executor(None, next, self._iterator, self)
        if value is self:
            raise StopAsyncIteration
        return value


async def main():
    async for i in AsyncIter([1, 2, 3]):
        print(i)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
