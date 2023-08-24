from sqlalchemy.orm import declarative_base
from sqlalchemy import Table, Integer, Column, String

class Usuario(declarative_base()):
    __tablename__ = 'usuario'
    
    id       = Column(Integer(), primary_key=True)
    nome     = Column(String(255), nullable=False)
    idade    = Column(Integer(), nullable=False)
    endereco = Column(String(255), nullable=False)
    senha    = Column(String(255), nullable=False)
    cpf      = Column(String(11), nullable=False)
    
    def __repr__(self) -> str:
        return f"ID: {self.id}, Nome: {self.nome}, Idade: {self.idade}, Endereco: {self.endereco}, Senha: {self.senha}, CPF: {self.cpf}"
    
    def _as_dict(self) -> dict:
        dict_user = {
                     "id"      : {self.id},
                     "nome"    : {self.nome},
                     "idade"   : {self.idade},
                     "endereco": {self.endereco},
                     "senha"   : {self.senha},
                     "cpf"     : {self.cpf}
                    }
        return dict_user
    