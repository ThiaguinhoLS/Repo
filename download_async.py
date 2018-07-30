#!usr/bin/python3.6
# -*- coding: utf-8 -*-

import asyncio
import aiohttp
import aiofiles as aiof


async def save_file():
    async with aiof.open('blah.txt', 'w') as f:
        await f.write('...')


async def main():
    async with aiohttp.ClientSession() as session:
        pass


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(save_file())
    loop.close()
