#!usr/bin/python3
# -*- coding: utf-8 -*-

import asyncio
import aiohttp


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect('http://example.org/ws') as ws:
            async for message in ws:
                if message.type == aiohttp.WSMsgType.TEXT:
                    if message.data == 'close cmd':
                        await ws.close()
                        break
                    else:
                        await ws.send_str(msg.data + '/answer')
                elif message.type == aiohttp.WSMsgType.ERROR:
                    break


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
