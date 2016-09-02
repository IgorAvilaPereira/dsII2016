# -*- coding: utf-8 -*-
from flask import *
from simple_page import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page, url_prefix='/simple_page')

@app.route("/")
def index():
	vetItem = ["http://www.google.com", "http://g1.com"]
	return render_template("index2.html", vetItem = vetItem, mensagem = "Oi Igor...")

if __name__ == "__main__":
	app.debug = True
	app.run()
