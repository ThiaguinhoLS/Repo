#!usr/bin/python3
# -*- coding: utf-8 -*-

import asyncio
import aiohttp


async def main():
    url = 'http://example.com/image'
    payload = b'GIF89a\x01\x00\x01\x00\x00\xff\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x00;'
    headers = {'content-type': 'image/gif'}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=headers) as response:
            print(response.status)
            print(await response.text())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
