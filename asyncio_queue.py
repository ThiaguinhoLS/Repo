#!usr/bin/python3
# -*- coding: utf-8 -*-

import asyncio
import time
import random

async def news_producer(my_queue):

    while True:
        await asyncio.sleep(3)
        print('Inserindo um novo item na queue')
        await my_queue.put(random.randint(1, 5))


async def news_consumer(id, my_queue):
    
    print(my_queue)
    while True:
        print(f'Consumidor : {id} removendo itens da queue')
        item = await my_queue.get()
        if item is None:
            break
        print(f'Consumer: {id} removeu {item}')


if __name__ == '__main__':
    my_queue = asyncio.Queue(maxsize=0)
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
                news_producer(my_queue),
                news_consumer(1, my_queue),
                news_consumer(2, my_queue)
            )
        )
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
        
