#connection.py
from sqlalchemy import create_engine
from Utils.Constants import DATA_BASE_URL
from Entities.Usuario import Usuario
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:

    def __init__(self) -> None:
        self.__engine = self.__create_database_engine()
        self.session  = None
    
    def __create_database_engine(self):
        return create_engine(DATA_BASE_URL)
        
    def __enter__(self):
        session = sessionmaker(bind=self.__engine)
        self.session = session()
        return self

    def __exit__(self, exec_type, exec_val, exec_tb):
        self.session.close()


# try:
#     for usuario in session.query(Usuario):
#       print(usuario)
# except (ConnectionAbortedError) as error:
#     print("conexao com banco abortado: "+ error)
