import operations

class App():
    
    def __init__(self) -> None:
        self.db_connection = operations.DB_CONNECTION()
    
    
    def run():
        # run application
        while True:
            pass
            
        return False


if __name__ == "__main__":
    app = App()
    
    try:
        if app.db_connection.connect():
            print("conexao criada")
        
    except(ConnectionError) as error:
        print("Falha em se conectar no banco", error)