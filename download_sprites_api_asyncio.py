#!usr/bin/python3
# -*- coding: utf-8 -*-

import asyncio
import aiohttp
import aiofiles as aiof
import shutil
import os

PATH = 'sprites'


def decorator(path, coro=None):
    if coro is None:
        return lambda coro: decorator(path, coro)
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)
    return coro


async def download(session, url, name):
    async with session.get(url) as response:
        async with aiof.open(os.path.join(PATH, name) + '.png', mode='wb') as f:
            while True:
                chunk = await response.content.read(1024)
                if not chunk:
                    break
                await f.write(chunk)
    print(f'Download concluído com sucesso: {name}')


async def get_image(session, **kwargs):
    async with session.get(kwargs['url']) as response:
        return (await response.json())['sprites']['front_default'], kwargs['name']
    

async def fetch(session, url, params=None):
    if params is None:
        params = {}
    async with session.get(url, params=params) as response:
        return (await response.json())['results']


@decorator(PATH)
async def main():
    params = {'limit': 100}
    tasks_download = []
    async with aiohttp.ClientSession() as session:
        results = await fetch(session, 'http://pokeapi.co/api/v2/pokemon/', params)
        tasks = [asyncio.ensure_future(get_image(session, **data)) for data in results]
        for task in asyncio.as_completed(tasks):
            url, name = await task
            tasks_download.append(asyncio.ensure_future(download(session, url, name)))
        await asyncio.gather(*tasks_download)
        
            


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
