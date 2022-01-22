import animal

class Gato(animal.Animal):
    habilidade = 'miar'

    def __init__(self, idade=int, sexo=str):
        self.idade =  idade
        self.sexo = sexo

    def Habilidade(self):
        return super().Habilidade(self.habilidade)

    def getIdade(self):
        return self.idade

    def getSexo(self):
        return self.sexo

if __name__ == '__main__':
    
    gato_A = Gato(idade=5, sexo='Masculino')
    gato_A.Habilidade()