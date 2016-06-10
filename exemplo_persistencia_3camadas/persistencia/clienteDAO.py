import sys
sys.path.append("./negocio")

from conexao import Conexao
from cliente import Cliente

class ClienteDAO:

	def __init__(self, conexao):
		self.deleteSQL = "DELETE FROM cliente WHERE id = %s"
		self.selectTodosSQL = "SELECT * FROM cliente"
		self.updateSQL = "UPDATE cliente SET nome = %s, endereco = %s, matricula = %s WHERE id = %s"
		self.insertSQL = "INSERT INTO cliente (nome, endereco, matricula) VALUES(%s,%s, %s)"
		self.conexao = conexao	
		

	def listaTodos(self):
		self.conexao.cur.execute(self.selectTodosSQL)			
		linhasRetornadas = self.conexao.cur.rowcount; #linhas afetadas de um select
		#print linhasRetornadas
		vetCliente = []
		i = 0
		while(i < linhasRetornadas):
			registro = self.conexao.cur.fetchone()
			vetCliente.append(Cliente(registro[1], registro[2], registro[3], registro[0]))
			i = i + 1	
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
