from cliente import Cliente

class Dependente(object):
	
	def __init__(self, nome, genero = None, cliente = Cliente(), id = None):
		self.id = id
		self.nome  = nome
		self.cliente = cliente
		self.genero = genero



