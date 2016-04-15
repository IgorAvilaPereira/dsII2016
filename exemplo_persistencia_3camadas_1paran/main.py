import sys
sys.path.append("./negocio")
sys.path.append("./persistencia")

from cliente import Cliente #negocio
from dependente import Dependente #negocio
from clienteDAO import ClienteDAO #persistencia
from dependenteDAO import DependenteDAO #persistencia
from conexao import Conexao #persistencia


# http://initd.org/psycopg/

conexao = Conexao("trabalho")
clienteDAO = ClienteDAO(conexao)

vetCliente = clienteDAO.listaTodos()
cliente = vetCliente[5]
print str(cliente.id) + ":" + cliente.nome
for dep in cliente.vetDependente:
	print str(dep.id) + ":" + dep.nome 


novoCliente = Cliente("Novo Igor", "Novo Quiosque", 1111111)
novoCliente.adicionarDependente(Dependente("dep 1 de 10", "trans"))
clienteDAO.inserir(novoCliente)

novoDependente = Dependente("deve dar erro", "hercules")
novoDependente.cliente = novoCliente
DependenteDAO(conexao).inserir(novoDependente)

conexao.encerra()


