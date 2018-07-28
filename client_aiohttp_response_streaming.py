#!usr/bin/python3
# -*- coding: utf-8 -*-

import asyncio
import aiohttp
import aiofiles as aiof


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(
            'https://i.pinimg.com/originals/4c/21/17/4c2117489c9bbe6a6a007de70b9a4c5b.jpg'
        ) as response:
            async with aiof.open('image.jpg', mode='wb') as f:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    await f.write(chunk)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
