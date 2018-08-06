#!usr/bin/python3
# -*- coding: utf-8 -*-

import asyncio

async def coro():
    while True:
        await asyncio.sleep(1)
        print('Task executada')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        asyncio.ensure_future(coro())
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print('Fechando o loop')
        loop.close()
