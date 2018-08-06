#!usr/bin/python3
# -*- coding: utf-8 -*-

import asyncio


async def bar(number):
    print(f'Enter bar {number}')
    await asyncio.sleep(number)
    print(f'Exit bar {number}')
    if number % 2 == 0:
        return True
    #raise asyncio.CancelledError('Cancelada')
    raise ValueError


async def main():
    tasks = [asyncio.ensure_future(bar(n)) for n in range(1, 6)]
    # Se return_exceptions for definido como True se a corotina levantar uma exceção a mesma será suprimida
    for task in await asyncio.gather(*tasks, return_exceptions=False):
        print(task)
    

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
