#connection.py
from sqlalchemy import create_engine
from Utils.Constants import DATA_BASE_URL
from Entities.Usuario import Usuario
from sqlalchemy.orm import sessionmaker

# cria engine
engine = create_engine(DATA_BASE_URL)

# cria sessão -> Sessao a partir da engine conectado com o banco
Session = sessionmaker(bind=engine)
session = Session()

user1 = Usuario(
    nome = "matheus12",
    idade = 10,
    endereco = "123",
    senha = "123",
    cpf = "123"
)

try:
    for usuario in session.query(Usuario):
      print(usuario)
except (ConnectionAbortedError) as error:
    print("conexao com banco abortado: "+ error)
