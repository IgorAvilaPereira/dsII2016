# -*- coding: utf-8 -*-


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/aula2_sqlalchemy'
# notificacoes
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

funcionario_projeto = db.Table( 'funcionario_projeto' ,
    db.Column( 'funcionario_id' , db.Integer, db.ForeignKey( 'funcionario.id' ), primary_key=True),
    db.Column( 'projeto_id' , db.Integer, db.ForeignKey( 'projeto.id' ), primary_key=True),
#    db.Column('data_inicio', db.Date),
#    db.Column('data_fim', db.Date)
)

class Funcionario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    projeto = db.relationship( 'Projeto' , secondary = 'funcionario_projeto', backref = db.backref( 'pages' , lazy = 'dynamic' ))
    def __repr__(self):
        return self.nome

class Projeto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))

# rota inicial => index
@app.route("/")
def hello():
    funcionario1 = Funcionario.query.get(1)
    #projeto = Projeto.query.get(1)
    #    print funcionario1
    """
        functionario2 = Funcionario.query.get(2)
        print functionario2
        vetFuncionario = Funcionario.query.all()
        print vetFuncionario
        html = ""
        print len(vetFuncionario)
        i = 0
        while (i < 2):
            print "oi"
            print i
            html +=  vetFuncionario[i].nome
            i = i + 1
    """
    return funcionario1.nome + ":" + funcionario1.projeto[0].nome

if __name__ == "__main__":
    # para destruir
    #db.drop_all()
    # para criar as tabelas
    #db.create_all()
    # habilitar o debug no flask
    app.debug = True
    # rodar aplicacao
    app.run()
