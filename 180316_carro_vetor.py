# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 10:06:35 2016

@author: iapereira
"""

"""class Carro:
    
    def __init__(self, consumo):
        self.combustivel = 0.0
        self.consumo = float(consumo)
    
    def mover(self, distancia):
        c = distancia * self.consumo
        if (c < 0):
            return False
        else:
            self.combustivel = self.combustivel - c
    def abastecer(self, combustivel):
        self.combustivel = self.combustivel + combustivel
    
    def gasolina(self):
        return self.combustivel

carro = Carro(5)
carro.abastecer(220)
carro.mover(20)
print carro.gasolina()"""

class Vetor:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    
    def __add__(self, vet):
        x = self.x + vet.x
        y = self.y + vet.y
        z = self.z + vet.z
        return Vetor(x, y, z)
        
    def __sub__(self, vet):
        x = self.x - vet.x
        y = self.y - vet.y
        z = self.z - vet.z
        return Vetor(x, y, z)
    
    def pEscalar(self, vet):
        return (self.x * vet.x) + (self.y * vet.y) + (self.z * vet.z)
    
    def __mul__(self, vet):
        x = (self.y * vet.z) - (self.z * vet.y)
        y = (self.x * vet.z) - (self.z * vet.x)
        z = (self.x * vet.y) - (self.y * vet.x)
        return Vetor(x, y, z)

vetor1 = Vetor(3, 2, 5)
vetor2 = Vetor(3, 4, 5)

print vetor1.pEscalar(vetor2)

vetor3 = vetor1 + vetor2
print str(vetor3.x)+', '+str(vetor3.y)+', '+str(vetor3.z)























































        
        