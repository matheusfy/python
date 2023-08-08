import psycopg2
import configparser

c_SqlFile = "C:/Users/mathe/Documents/Desenvolvimento/python/CRUD/configfile.ini"

class DB_CONNECTION():
    
    def __init__(self) -> None:
        self.__connection = None
        self.__config_obj = configparser.ConfigParser()
        
    def connect(self) -> bool:
        try:
            self.__config_obj.read(c_SqlFile)
            dbparam = self.__config_obj["postgresql"]
        except(Exception) as error:
            print("Falho em abrir o arquivo config", error)
            return False

        try:
        # set your parameters for the database connection URI using the keys from the configfile.ini
            user     = dbparam["user"]
            password = dbparam["password"]
            host     = dbparam["host"]
            dbase    = dbparam["db"]
            port     = int(dbparam["port"])
            
            # Connect to the database
            self.__connection = psycopg2.connect(user       = user,
                                                        password = password,
                                                        host     = host,
                                                        port     = port,
                                                        database = dbase)
        except (Exception, psycopg2.Error) as error:
            print("Falha em conectar ao banco.", error)
            return False

        return True
    
    def CreateTable(self):
        pass
    
    def Insert(self):
        pass
    
    def Update(self):
        pass
    
    def Update(self):
        pass

    def Delete(self):
        pass