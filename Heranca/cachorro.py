import animal

class Cachorro(animal.Mamifero):

    habilidade = 'latir'

    def __init__(self, idade=int, sexo=str):
        self.idade =  idade
        self.sexo = sexo

    def Habilidade(self,):
        return super().Habilidade(self.habilidade)  # Pega o método do pai

    def getIdade(self,):
        return self.idade

    def getSexo(self,):
        return self.sexo

if __name__ == '__main__':
    
    cachorro_A = Cachorro(idade=5, sexo='Masculino')
    cachorro_A.Habilidade()
