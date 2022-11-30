#Python Dependency Inversion Principle
#Thamires Lemes Leal

# Exemplo Incorreto


def cozinhar(comida: str):
    if comida == "pao":
        pao = Pao()
        pao.assar()
    if comida == "biscoito":
        biscoito = Biscoito()
        biscoito.assar()

cozinhar("biscoito")






# Exemplo Correto

from abc import ABC, abstractmethod
class Assado(ABC):
    @abstractmethod
    def assar(self):
        pass

#Módulo de alto nível, é o módulo principal que realiza uma atividade mais próxima da realidade. 
#Por exemplo cozinhar, que é uma atividade que faz parte do dia a dia de qualquer pessoa.
def cozinhar(assado:Assado):
    assado.assar()
    

#Módulo de baixo nível, é o módulo que realiza uma atividade mais próxima da tecnologia.
#Módulo que realiza uma atividade mais próxima da tecnologia, por exemplo, assar.
class Pao(Assado):
    def assar(self):
        print('Assou pão')
        
        
class Biscoito(Assado):
    def assar(self):
        print('Assou biscoito')