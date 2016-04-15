
class Cliente (object):

	def __init__(self, nome = None, endereco = None, matricula = None, id = 0):
		self.id = id
		self.nome = nome
		self.endereco = endereco
		self.matricula = matricula
		self.vetDependente = []

	def adicionarDependente(self, dependente):
		self.vetDependente.append(dependente)	
		dependente.cliente = self

	def __repr__(self):
		return str(self.id) + ";" + self.nome + ";" + self.endereco +";" + str(self.matricula)
