#!usr/bin/python3
# -*- coding: utf-8 -*-

import asyncio
import aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://google.com') as response:
            print('Status code:', response.status)
            print('Conteúdo da resposta:', await response.text())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
