import sys
sys.path.append("./negocio")
sys.path.append("./persistencia")

from cliente import Cliente #negocio
from clienteDAO import ClienteDAO #persistencia
from conexao import Conexao #persistencia


# http://initd.org/psycopg/

conexao = Conexao("trabalho")
#conexaoOutroBanco = Conexao("youtube")
clienteDAO = ClienteDAO(conexao)
"""
registroLucas = clienteDAO.listaTodos()[1]
clienteLucas = Cliente(registroLucas[1], registroLucas[2], registroLucas[3], registroLucas[0])
#print clienteLucas

clienteLucas.matricula = 11030189
clienteDAO.alterar(clienteLucas)


novoCliente = Cliente("Augusta", "Subway", 11030176)
clienteDAO.inserir(novoCliente)
"""

print clienteDAO.listaTodos()

conexao.encerra()