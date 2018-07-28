#!usr/bin/python3
# -*- coing: utf-8 -*-

import asyncio
import aiohttp
import ujson


async def main():
    async with aiohttp.ClientSession(json_serialize=ujson.dumps) as session:
        async with session.post('http://google.com', json={'test': 'object'}) as response:
            print(await response.text())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
