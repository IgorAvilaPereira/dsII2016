import psycopg2

class Cliente (object):

	def __init__(self, nome = None, endereco = None, matricula = None, id = 0):
		self.id = id
		self.nome = nome
		self.endereco = endereco
		self.matricula = matricula

	def __repr__(self):
		return str(self.id) + ";" + self.nome + ";" + self.endereco +";" + str(self.matricula)

class Conexao:

	def __init__(self, dbname, host = "localhost", user = "postgres" , password = "postgres" ):
		try:
			self.conn = psycopg2.connect("host="+host+" dbname="+dbname+" user="+user+" password="+password)
			self.cur = self.conn.cursor()
		except:
			print "Deu xabum na conexao...."
			exit()	

	def encerra(self):
		self.cur.close()
		self.conn.close()		



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
