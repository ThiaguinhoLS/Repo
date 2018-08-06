#!usr/bib/python3
# -*- coding: utf-8 -*-

from threading import Thread, Event
from queue import Queue
from urllib.parse import urljoin
from requests import get
from time import sleep, time
from shutil import copyfileobj, rmtree
from os import mkdir
from os.path import exists
from contextlib import contextmanager


@contextmanager
def timeit():
    start = time()
    yield
    print('Encerrou em {:.3f}'.format(time() - start))


def get_bin_file(args):
    name, url = args
    print('get_bin', name, url)
    return name, get(url, stream=True)


def save_file(args, path=path, ext='png'):
    name, binary = args
    print('save_file', name, binary)
    filename = f'{path}/{name}.{ext}'
    print(filename)
    with open(filename, mode='wb') as f:
        for chunk in binary.iter_content(chunk_size=128):
            f.write(chunk)


def get_sprite_url(args, sprite='front_default'):
    print('get_sprite', args)
    return args['name'], get(args['url']).json()['sprites'][sprite]


def get_urls():
    pokemons = get(base_url, params={'limit': 1}).json()['results']
    [q.put(pokemon) for pokemon in pokemons]
    event.set()
    q.put(None)


def get_pool(number):
    return [Worker(target=target, queue=q, name=f'Worker {n}') for n in range(number)]


class Worker(Thread):

    def __init__(self, target, queue, *, name='Worker'):
        super().__init__()
        self._target = target
        self.queue = queue
        self.name = name
        self._stopped = False
        print(f'Inicializado {name}')

    def run(self):
        event.wait()
        while not self.queue.empty():
            item = self.queue.get()
            if item is None:
                q.put(None)
                self._stopped = True
                break
            self._target(item)

    def join(self):
        while not self._stopped:
            sleep(0.1)

    @classmethod
    def get_pool(klass, number):
        return [klass(target=target, queue=q, name=f'Worker {n}') for n in range(number)]
        

def pipeline(*funcs):
    def inner(argument):
        state = argument
        for func in funcs:
            state = func(state)
    return inner
           

if __name__ == '__main__':
    base_url = 'http://pokeapi.co/api/v2/pokemon/'
    event = Event()
    q = Queue(maxsize=0)
    path = 'sprites'
    if exists(path):
        rmtree(path)
    mkdir(path)
    with timeit():
        get_urls()
        target = pipeline(get_sprite_url, get_bin_file, save_file)
        t_one = Worker(target=target, queue = q, name='Worker one')
        t_one.start()
        t_one.join()
##        threads = Worker.get_pool(3)
##        print(threads)
##        for t in threads: t.start()
##        for t in threads: t.join()
            
    
