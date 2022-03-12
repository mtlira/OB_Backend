from setup import db
from model.business.basemodel import BaseModel
from sqlalchemy import Table, Column, Integer, ForeignKey, MetaData, select
from setup import db
from sqlalchemy.ext.serializer import loads, dumps

metadata_obj = MetaData()
metadata_obj.reflect(bind=db.engine)
Familia = metadata_obj.tables['familia']
Usuario = metadata_obj.tables['usuario']
Conta = metadata_obj.tables['conta']
Movimentacao = metadata_obj.tables['movimentacao']

print(Familia.c.keys)
#amilia = Table("familia", db.metadata, autoload_with = db.engine)
#Usuario = Table("usuario", db.metadata, autoload_with = db.engine)
#Conta = Table("conta", db.metadata, autoload_with = db.engine)
#Movimentacao = Table("familia", db.metadata, autoload_with = db.engine)

#print(Usuario.c.keys(), Familia, Movimentacao.c.keys())

#with db.engine.connect() as conn:
#    result =  db.session.execute(select(Usuario))
#    for row in result.mappings():
#        print(row)


