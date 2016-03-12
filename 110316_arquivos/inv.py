# -*- coding: utf-8 -*-

file = open('sequencia.txt')
v = file.readlines()
file.close()
vok = []

for valor in v:
    vok.append(valor.strip())

inv = vok[::-1]

new_file = open('inv.txt', 'w')

new_file.write(str(inv))

new_file.close()
