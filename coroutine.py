# -*- coding: utf-8 -*-
import asyncio

async def coroutine(value):
    await asyncio.sleep(1)
    return value

# Instância o loop de eventos
loop = asyncio.get_event_loop()
# Cria uma task
task = loop.create_task(coroutine(1))
# Adiciona uma função de callback a task
task.add_done_callback(lambda future: loop.stop())
# Faz o loop de eventos rodar infinitamente
loop.run_forever()
# Fecha o loop de eventos
loop.close()

