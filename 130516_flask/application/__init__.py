from flask import *

app = Flask(__name__)
app.secret_key = "\x91XC\x82\x97\x10X\x9e@\xfa\x9b\xf6WO\x18\xdd\nr\xce\xb6r\x96\xfdF"

"""
@app.errorhandler(404)
def error404(error):
	return "ops...."
"""

@app.errorhandler(404)
def error404(error):
	return render_template("404.html")
	#return "Pagina nao encontrada...."

def mostra_formulario_login():
	#abort(401)
	#html = "<form action = 'http://localhost:5000/login' method = 'POST'>"
	#html = html + "Login: <input type='text' name='login'> <br>"
	#html = html + "Senha: <input type='password' name='senha'> <br>"
	#html = html + "<input type='submit'>"
	#html = html + "</form>"
	#return html
	flash("faca aqui seu login....")
	return render_template("formulario.html")


@app.route("/testabootstrap")
def testabootstrap():
	#pessoaDAO = pessoaDAO()
	#vetCliente = pessoaDAO.select()
	clientes = ["Igor","Bernardo"]
	nome = "Igor"
	return render_template("testabootstrap.html", vetCliente = clientes, login = session['login'])


def autenticacao():
	#abort(404)
	mensagem = "Login:"+request.form['login'] + " Senha:"+request.form['senha']
	session['login'] = request.form['login']
	session['senha'] = request.form['senha']
	return render_template("autenticacao.html", mensagem = mensagem)	 

@app.route("/login", methods =['GET', 'POST'])
def login():
	if request.method == 'POST':
		return autenticacao()
	else:
		return mostra_formulario_login()	

@app.route("/")
def index():
	return redirect(url_for("login"))

if __name__ == "__main__":
	app.debug = True
	app.run()