# -*- coding: utf-8 -*-
import numpy
file = open('matriz.txt', 'r')
conteudo = file.readline()
vetLinha =  conteudo.split("*")
vetLinhaVerdadeiroInt = []
matriz = []
for linha in vetLinha:
    vetLinhaVerdadeiro = linha.split(";")
    vetLinhaVerdadeiroInt = []
    for x in vetLinhaVerdadeiro:
        vetLinhaVerdadeiroInt.append(int(x))
    matriz.append(vetLinhaVerdadeiroInt)
file.close()
print matriz
# matriz transposta - metodo 1
Z = numpy.matrix(matriz)
print Z.T
# matriz tranposta - metodo 2
print zip(*matriz)
new_file = open ("tranposta.txt","w")
new_file.write(str(zip(*matriz)))
new_file.close()


