#!usr/bin/python3
# -*- coding: utf-8 -*-

from queue import Queue


def do_stuff(q):
    # Verifica se a queue está vazia
    while not q.empty():
        # Retorna o primeiro item da queue
        print(q.get())
        # Gera um ValueError se chamado mais vezes do que items colocados na queue, indica que terminou
        q.task_done()


if __name__ == '__main__':
    q = Queue(maxsize=0) # Instância uma queue com tamanho infinito
    for i in range(5):
        q.put(i) # Insere um item no final da queue
    do_stuff(q)
