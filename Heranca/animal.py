from abc import ABC, abstractclassmethod, abstractmethod



class Animal():
    idade = ''
    sexo = ''

    @abstractclassmethod
    def Habilidade(self, acao=str):
        print("Eu sei: "+ acao)


class Mamifero(Animal):

    @abstractclassmethod
    def Habilidade(self, acao=str):
        print("Eu sei: "+ acao)


class Passaro(Animal):

    @abstractclassmethod
    def Habilidade(self, acao=str):
        print("Eu sei: "+ acao)