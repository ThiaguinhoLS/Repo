#!usr/bin/python3
# -*- coding: utf-8 -*-

import asyncio
import time


async def myWorker(semaphore):
    await semaphore.acquire()
    print('Semáforo adquirido com sucesso')
    await asyncio.sleep(1)
    print('Semáforo liberado')
    semaphore.release()


async def main(loop):
    mySemaphore = asyncio.Semaphore(value=2)
    await asyncio.wait([myWorker(mySemaphore) for _ in range(4)])
    print('Corotina principal')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    print('Todos os workers completados')
    loop.close()

    
### Output ###

## Semáforo adquirido com sucesso
## Semáforo adquirido com sucesso
## Semáforo liberado
## Semáforo adquirido com sucesso
## Semáforo liberado
## Semáforo liberado
## Corotine principal
## Todos os workers completados
