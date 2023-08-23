from sqlalchemy import URL

DATA_BASE_URL = URL.create(
    "postgresql+psycopg2",
    username = "postgres",
    password = "nkrevg32",
    host     = 'localhost',
    port     = 5432,
    database = "cadastro"
)


# DATA_BASE_URL = 'postgresql+psycopg2://postgres:nkrevg32@localhost/cadastro'
SQL_FILE = "C:/Users/mathe/Documents/Desenvolvimento/python/CRUD/configfile.ini"