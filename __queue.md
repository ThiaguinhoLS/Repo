## Módulo queue do Python ##

_### queue.Queue(maxsize=0) ###_

Se `maxsize=0` a queue terá tamanho infinito, e o `queue.Queue.full()` sempre retornára `False`.

_### queue.Queue.empty() ###_

Retorna True caso a queue esteja vazia.

_### queue.Queue.maxsize ###_

Retorna o tamanho máximo da queue.

_### queue.Queue.full() ###_

Retorna True se a queue estiver com seu tamanho máximo.

_### queue.Queue.put(item, block=True, timeout=None) ###_

Insere o item ao final da queue. Se `block=True` e timeout=None bloqueia até que um slot esteja disponível dentro 
desse limite de tempo e aumentará `queue.Full` caso o tempo limite acabe. Se `block=False` insere o item imediamente 
e aumentará `queue.Full` caso não possua slots livres.

_### queue.Queue.get(block=True, timeout=None) ###_

Retorna o primeiro item da queue. Se não houver um item na queue bloqueia se necessário se `block=True` até que um 
item esteja disponível ou que `timeout` aumente queue.Empty.

_### queue.Queue.task_done() ###_

Indica que a tarefa anteriormente enfileirada está concluída. Aumentará ValueError se chamando mais vezes do que o
tamanho da queue.


```python
>>> from queue import Queue
>>> q = Queue(maxsize=2)
>>> q.maxsize
2
>>> q.empty()
True
>>> q.full()
False
>>> q.put(1)
>>> q.queue
deque([1])
>>> q.empty()
False
>>> q.put(2)
>>> q.queue
deque([1, 2])
>>> q.full()
True
>>> q.get()
1
>>> q.task_done()
>>> q.put(3)
>>> q.qsize()
2
```
