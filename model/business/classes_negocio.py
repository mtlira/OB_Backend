from app import app, db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata_obj = MetaData()
metadata_obj.reflect(bind=db.engine)

Familia = metadata_obj.tables['familia']
Usuario = metadata_obj.tables['usuario']
Conta = metadata_obj.tables['conta']
Movimentacao = metadata_obj.tables['movimentacao']