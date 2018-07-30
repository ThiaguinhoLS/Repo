#!usr/bin/python3
# -*- coding: utf-8 -*-

import asyncio
import aiofiles


async def write_file(filename):
    async with aiofiles.open(filename, mode='w') as f:
        await f.write('Blah Blah ...')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(write_file('blah.txt'))
    loop.close()
