# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 08:14:33 2016

@author: iapereira
"""

class Pessoa:
        def __init__(self, nome = '', sobrenome = '' ):
            self.nome = nome
            self.sobrenome = sobrenome
    
        def imprimeNomeCompleto(self):        
            return self.nome + " " + self.sobrenome   
        
        @staticmethod      
        def x():
            print 'oi'        
        
        def __repr__(self):
            return "Chamando meu __repr__:" + self.nome + " "+self.sobrenome
          
    
augusta = Pessoa()
print augusta


class Quadrado:
    def __init__ (self, lado):
         self.lado = lado
         
    def area(self):
        return self.lado * self.lado
        
        
quadradinhode8 = Quadrado(8)
print str(quadradinhode8.area())













        
    
    