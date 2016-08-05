from flask import Flask

# Adicionando importacao sqlAlchemy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/aula_sqlalchemy'
# notificacoes
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 

# relacionar a aplicacao flask com o sqlalchemy - criando um objeto db
db = SQLAlchemy(app)

# a classe User deve herdar db.Model
class User(db.Model):
	# coluna id => definindo a chave primaria
	id = db.Column(db.Integer, primary_key=True)
	# coluna username 
	username = db.Column(db.String(80), unique=True)
	# coluna email
	email = db.Column(db.String(120), unique=True)
	# construtor
	def __init__(self, username, email):
		self.username = username
		self.email = email
	# metodos....
	def __repr__(self):
		return '<User %r>' % self.username

@app.route("/listar")
def listar():
	# selecionando todos
	#vetUser = User.query.all()
	# usando filtro
	userIapereira = User.query.filter_by(username='iapereira').first()
	"""
	resultado = ""
	for i in range(0, len(vetUser)):
		resultado += vetUser[i].username + "<br>"
	return resultado
	"""
	return userIapereira.username


# rota inicial => index
@app.route("/")
def hello():
	# criando o objeto que pretendo adicionar
	#user = User("iapereira","igor.pereira@riogrande.ifrs.edu.br")
	# propondo que vou adicionar
	#db.session.add(user)
	usuario = User.query.get(1)
	db.session.delete(usuario)
	# fechando a transacao
	db.session.commit()
	# mensagem de sucesso...da adicao => retornando o user.username
	return "Usuario sdiufhusdifhsdifhidus:"

if __name__ == "__main__":
	# para criar as tabelas 
	#db.create_all() 
	# habilitar o debug no flask
	app.debug = True   
	# rodar aplicacao
	app.run()