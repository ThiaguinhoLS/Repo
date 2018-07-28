#!usr/bin/python3
# -*- coding: utf-8 -*-

import asyncio
import aiohttp


async def main():
    data = {
        'key': 'value',
    }
    async with aiohttp.ClientSession() as session:
        async with session.post('http://google.com', data=data) as response:
            print(await response.text())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
