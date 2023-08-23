from sqlalchemy import Table, Integer, Column, String, ForeignKey
from sqlalchemy.orm import registry
from Entities import Usuario


mapper_registry = registry()

usuario_table = {
    "usuario",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("nome", String(255)),
    Column("idade", Integer),
    Column("endereco", String(255)),
    Column("senha", String(255)),
    Column("cpf", String(255))
}

mapper_registry.map_imperatively(Usuario, usuario_table)