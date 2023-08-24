from connection import DBConnectionHandler
from Entities.Usuario import Usuario


class UsuarioRepository:

    def get_user(self, user):
        pass
    
    def get_users(self) -> list:
        lstUsers = []
        try:
            with DBConnectionHandler() as db:
                lstUsers = db.session.query(Usuario).all()
        except (Exception) as error:
            print(error)
        return lstUsers
    
    def add_user(self, user):
        pass
    
    def add_users(self, lstUsers):
        pass
    
    def update_user(self, user):
        pass
    
    def delete_user(self, id):
        pass
    