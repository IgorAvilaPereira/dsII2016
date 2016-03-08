# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 11:20:39 2016

@author: iapereira
"""

def listas(lista):
    lista.sort()
    return lista
    
def cortarlista(lista):
    n = int(raw_input("Digite onde deseja cortar: "))
    f = int(raw_input("Digite onde deseja fazer o segundo corte: "))
    return lista[n:f+1]

def mudarstring(palavra):
    return palavra[::-1]
   
def fatorial(numero):
    if numero == 1 or numero == 0:
        return 1
    else:
        return numero * fatorial(numero-1)

def fibonacci(elemento):
    if elemento == 1 or elemento == 2:
        return 1
    else:
        return fibonacci(elemento-1) + fibonacci(elemento - 2)
def maxmin(lista):
    moda = 0
    valordemoda = 0    
    lista.sort()
    print lista[0]
    print lista[-1]    
    for x in lista:
        quantidade = 0        
        for p in lista:
            if x == p:
                quantidade = quantidade + 1
        if quantidade > moda:
            moda =  quantidade
            valordemoda = x
    return valordemoda
    
def iguais(lista, lista2):
    listaresult = []
    jatem = False
    for p in lista:
        for x in lista2:
            if p == x:
                for w in listaresult:
                    if w == p:
                        jatem = True
                if jatem == False:        
                    listaresult.append(p)
                else:
                    jatem = False
    return listaresult

def dic(dicionario):    
    total = 0
    for x in dicionario.values():
        total = total + x
    return total    
    
    
    
    
    
    