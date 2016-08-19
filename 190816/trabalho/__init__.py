# -*- coding: utf-8 -*-
from flask import *

app = Flask(__name__)

@app.route("/")
def index():
	vetItem = ["http://www.google.com", "http://g1.com"]
	return render_template("index2.html", vetItem = vetItem, mensagem = "Oi Igor...")

if __name__ == "__main__":
	app.debug = True
	app.run()
