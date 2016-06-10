# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 10:34:39 2016

@author: iapereira
"""

file = open('sequencia.txt')
v = file.readlines()
file.close()

max = 0

for i in v:
    if int(i) > max:
        max = int(i)
print max

new_file = open('maior.txt', 'w')

new_file.write(str(max))

new_file.close()