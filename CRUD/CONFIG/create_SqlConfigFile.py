import configparser

config = configparser.ConfigParser()
# Add the structure to the file we will create
config.add_section('postgresql')
config.set('postgresql', 'host'    , 'localhost')
config.set('postgresql', 'user'    , 'postgres')
config.set('postgresql', 'port'    , '5432')
config.set('postgresql', 'password', 'nkrevg32')
config.set('postgresql', 'db'      , 'cadastro')

config.add_section('user_info')
config.set('user_info', 'admin'   , 'postgres')
config.set('user_info', 'login'   , 'postgres')
config.set('user_info', 'password', 'nkrevg32')

# Write the new structure to the new file


with open(r"C:\Users\mathe\Documents\Desenvolvimento\python\CRUD\configfile.ini", 'w') as configfile:
    config.write(configfile)