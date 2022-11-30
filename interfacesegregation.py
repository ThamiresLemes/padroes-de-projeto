#Python Interface Segregation Principle
#Thamires Lemes Leal

# Exemplo Incorreto

from abc import ABC, abstractclassmethod
class Animais(ABC):
    @abstractclassmethod
    def comer(self):
        pass    
    def dormir(self):
        pass
    def voar(self):
        pass
    
class Papagaio(Animais):
    def comer(self):
        print('Papagaio comendo')
    def dormir(self):
        print('Papagaio dormindo')
    def voar(self):
        print('Papagaio voando')
        
class Pinguim(Animais):
    def comer(self):
        print('Pinguim comendo')
    def dormir(self):
        print('Pinguim dormindo')
    def voar(self):
        raise Exception('Pinguim não voa')
    
# Exemplo Correto

class Necessidades(ABC):
    @abstractclassmethod
    def comer(self):
        pass
    def dormir(self):
        pass

class Voando(Necessidades):
    @abstractclassmethod
    def voar(self):
        pass

class Papagaio(Voando):
    def comer(self):
        print('Papagaio comendo')
    def dormir(self):
        print('Papagaio dormindo')
    def voar(self):
        print('Papagaio voando')
        
class Pinguim(Necessidades):
    def comer(self):
        print('Pinguim comendo')
    def dormir(self):
        print('Pinguim dormindo')