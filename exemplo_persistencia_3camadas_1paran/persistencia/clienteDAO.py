import sys
sys.path.append("./negocio")

from conexao import Conexao
from dependenteDAO import DependenteDAO
from cliente import Cliente

class ClienteDAO:

	def __init__(self, conexao):
		self.deleteSQL = "DELETE FROM cliente WHERE id = %s"		
		self.selectTodosSQL = "SELECT * FROM cliente order by id"
		self.updateSQL = "UPDATE cliente SET nome = %s, endereco = %s, matricula = %s WHERE id = %s"
		self.insertSQL = "INSERT INTO cliente (nome, endereco, matricula) VALUES(%s,%s, %s) RETURNING id"
		self.selectWithoutMatricula = "select * from cliente where matricula is null;"
		self.conexao = conexao	
		self.dependenteDAO = DependenteDAO(self.conexao)
		
	def listarSemMatricula(self):
		self.conexao.cur.execute(self.selectWithoutMatricula)			
		linhasRetornadas = self.conexao.cur.rowcount; #linhas afetadas de um select
		#print linhasRetornadas
		vetCliente = []
		i = 0
		while(i < linhasRetornadas):
			registro = self.conexao.cur.fetchone()
			vetCliente.append(Cliente(registro[1], registro[2], registro[3], registro[0]))
			i = i + 1	
		return vetCliente	
		
		
	def listaTodos(self):
		self.conexao.cur.execute(self.selectTodosSQL)
		vetCliente = []
		vetRegistro = self.conexao.cur.fetchall() 
		for registro in vetRegistro:
			novoCliente = Cliente(registro[1], registro[2], registro[3], registro[0])
			novoCliente.vetDependente = self.dependenteDAO.listarDependentesPorCliente(novoCliente)
			vetCliente.append(novoCliente)
		return vetCliente	

	def deletar(self, id):
		parametros = []
		parametros.append(id)
		self.conexao.cur.execute(self.deleteSQL, parametros)	
		self.conexao.conn.commit()

	def alterar(self, cliente):
		parametros = []
		parametros.append(cliente.nome)	
		parametros.append(cliente.endereco)
		parametros.append(cliente.matricula)
		parametros.append(cliente.id)
		self.conexao.cur.execute(self.updateSQL, parametros)	
		self.conexao.conn.commit()


	def inserir (self, cliente):
		parametros = []
		parametros.append(cliente.nome)	
		parametros.append(cliente.endereco)
		parametros.append(cliente.matricula)		
		self.conexao.cur.execute(self.insertSQL, parametros)	
		self.conexao.conn.commit()
		cliente.id = self.conexao.cur.fetchone()[0]
		for i in range(0, len(cliente.vetDependente)):
			self.dependenteDAO.inserir(cliente.vetDependente[i])	
