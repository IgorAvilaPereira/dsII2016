import sys
sys.path.append("./negocio")

from conexao import Conexao
from dependente import Dependente

class DependenteDAO:

	def __init__(self, conexao):
		self.deleteSQL = "DELETE FROM dependente WHERE id = %s"		
		self.selectTodosSQL = "SELECT * FROM dependente"
		self.selectDependentesPorClienteSQL = "SELECT * FROM dependente where cliente_id  = %s"
		self.updateSQL = "UPDATE dependente SET nome = %s, genero = %s, cliente_id = %s WHERE id = %s"
		self.insertSQL = "INSERT INTO dependente (nome, genero, cliente_id) VALUES(%s,%s, %s)"
		self.insertWithoutClienteSQL = "INSERT INTO dependente (nome, genero) VALUES(%s,%s)"
		#self.selectWithoutcliente_id = "select * from dependente where cliente_id is null;"
		self.conexao = conexao	
	
	def listarDependentesPorCliente(self, cliente):
		parametros = []
		parametros.append(cliente.id)
		self.conexao.cur.execute(self.selectDependentesPorClienteSQL, parametros)	
		linhasRetornadas = self.conexao.cur.rowcount; #linhas afetadas de um select
		vetdependente = []
		i = 0
		while(i < linhasRetornadas):
			x = self.conexao.cur.fetchone()
			vetdependente.append(Dependente(x[1], x[2], cliente, x[0]))
			i = i + 1	
		return vetdependente	

	"""	
	def listarSemcliente_id(self):
		self.conexao.cur.execute(self.selectWithoutcliente_id)			
		linhasRetornadas = self.conexao.cur.rowcount; #linhas afetadas de um select
		#print linhasRetornadas
		vetdependente = []
		i = 0
		while(i < linhasRetornadas):
			x = self.conexao.cur.fetchone()
			vetdependente.append(dependente(x[1], x[2], x[3], x[0]))
			i = i + 1	
		return vetdependente	
	"""	
		
	def listaTodos(self):
		self.conexao.cur.execute(self.selectTodosSQL)			
		linhasRetornadas = self.conexao.cur.rowcount; #linhas afetadas de um select
		#print linhasRetornadas
		vetdependente = []
		i = 0
		while(i < linhasRetornadas):
			x = self.conexao.cur.fetchone()
			vetdependente.append(dependente(x[1], x[2], x[3], x[0]))
			i = i + 1	
		return vetdependente	

	def deletar(self, id):
		parametros = []
		parametros.append(id)
		self.conexao.cur.execute(self.deleteSQL, parametros)	
		self.conexao.conn.commit()

	def alterar(self, dependente):
		parametros = []
		parametros.append(dependente.nome)	
		parametros.append(dependente.genero)
		parametros.append(dependente.cliente.cliente_id)
		parametros.append(dependente.id)
		self.conexao.cur.execute(self.updateSQL, parametros)	
		self.conexao.conn.commit()

	def inserir (self, dependente):
		try:
			parametros = []
			parametros.append(dependente.nome)	
			parametros.append(dependente.genero)
			parametros.append(dependente.cliente.id)		
			self.conexao.cur.execute(self.insertSQL, parametros)
			self.conexao.conn.commit()
		except:
			print "Dependente sem cliente ...."	
			exit()
