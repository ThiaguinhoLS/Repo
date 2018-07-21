# -*- coding: utf-8 -*-

class Singleton(object):

	'Classe que implementa o padrão de projeto Singleton'

	def __new__(klass, *args, **kwargs):
		if not hasattr(klass, '_instance'):
			klass._instance = object.__new__(klass)
			klass._instance._init(*args, **kwargs)
		return klass._instance

	def _init(self, *args, **kwargs):
		raise NotImplementedError()


class Spam(Singleton):

	'Classe que implementa o método _init que inicializa instância'

	def _init(self, value = None):
		self.value = value


def factory_singleton(_instance = Spam()):

	'Retorna somente uma única instância de Spam definida como argumento padrão'

	return _instance

def test_singleton_instance():

	'Testa se a classe Spam só cria uma única instância'
	
	assert Spam(1) is Spam(2)

def test_factory_singleton():
	assert factory_singleton() is factory_singleton()

def main():
	test_singleton_instance()

if __name__ == '__main__':
	main()


