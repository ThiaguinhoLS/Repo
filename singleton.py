# -*- coding: utf-8 -*-

class Singleton(object):

	def __new__(klass, *args, **kwargs):
		if not hasattr(klass, '_instance'):
			klass._instance = object.__new__(klass)
			klass._instance._init(*args, **kwargs)
		return klass._instance

	def _init(self, *args, **kwargs):
		raise NotImplementedError()


class Spam(Singleton):

	def _init(self, value):
		self.value = value


def factory_singleton(_instance = Spam()):
	'Retorna somente uma única instância de Spam definida como argumento padrão'
	return _instance

def test_singleton_instance():
	assert Spam() is Spam()

def test_factory_singleton():
	assert factory_singleton() is factory_singleton()

def main():
	test_singleton_instance()

if __name__ == '__main__':
	main()


