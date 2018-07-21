# -*- coding: utf-8 -*-
import asyncio

async def coroutine(value):
    await asyncio.sleep(1)
    return value

loop = asyncio.get_event_loop()
task = loop.create_task(coroutine(1))
task.add_done_callback(lambda future: loop.stop())
loop.run_forever()
loop.close()

