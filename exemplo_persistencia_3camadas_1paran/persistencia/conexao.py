import psycopg2

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