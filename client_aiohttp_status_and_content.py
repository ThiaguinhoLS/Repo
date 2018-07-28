#!usr/bin/python3
# -*- coding: utf-8 -*-

import asyncio
import aiohttp


async def fetch(session, url, params=None):
    if params is None:
        params = {}
    async with session.get(url, params=params) as response:
        print('Status code:', response.status)
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        content = await fetch(session, 'http://google.com')
        print('Conteúdo da resposta:', content)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
