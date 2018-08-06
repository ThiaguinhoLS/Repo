#!usr/bin/python3
# -*- coding: utf-8 -*-

import asyncio
import time

async def myWorker(lock, name):
    print(f'{name} entrará no lock')
    with await lock:
        print(f'{name} dentro do lock')
        time.sleep(3)
    print(f'{name} saiu do lock')


async def main():
    lock = asyncio.Lock()
    await asyncio.wait([myWorker(lock, 'worker one'), myWorker(lock, 'worker two')])


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
except KeyboardInterrupt as exc:
    pass
else:
    print('Todas as tasks completadas com sucesso')
finally:
    loop.close()
