from model.DAO import DAO
from json import dumps, JSONEncoder

from sqlalchemy.ext.declarative import DeclarativeMeta

from decimal import Decimal

class DecimalEncoder(JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Decimal):
      return str(obj)
    return JSONEncoder.default(self, obj)

def new_alchemy_encoder():
    _visited_objs = []

    class AlchemyEncoder(JSONEncoder):
        def default(self, obj):
            if isinstance(obj.__class__, DeclarativeMeta):
                # don't re-visit self
                if obj in _visited_objs:
                    return None
                _visited_objs.append(obj)

                # an SQLAlchemy class
                fields = {}
                for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata' and not x.startswith('query')]:
                    fields[field] = obj.__getattribute__(field)
                # a json-encodable dict
                return fields

            return JSONEncoder.default(self, obj)

    return AlchemyEncoder

class CTL_CentralizarContas:
    def centralizar():
        with open('login_info.txt') as file:
            info = file.readlines()
            idLogin = info[0].split()[1]
            emailLogin = info[1].split()[1]
        familia = DAO.getFamilia(idLogin, "centralizar")
        if familia != None:
            pessoas = familia.membros
            print("######################achou familia",familia.nome, familia.membros[0].nome)
        else:
            pessoas = [DAO.getUsuario(emailLogin)]
        
        # fetch/update users' accounts from OB
        # simulacao
        for i in range (0,len(pessoas)):
            pessoas[i].saldo_cc = Decimal(100.00 + 10.00*(i+1))
            pessoas[i].saldo_pp = Decimal(500.00 + 10.00*(i+1))
            pessoas[i].centralizar()
        
        dict = {}
        dict['usuarios'] = pessoas
        if familia != None: 
            familia.centralizar()
            dict['total_familia'] = familia.getCentralizedInfo()
        else: dict['total_familia'] = "None"
        #print("dict=\n",familia.to_dict(show = ['membros', 'membros.contas','membros.pagamentos','membros.recebimentos']))
        #print("usuario",pessoas[0].__dict__)
        #print("dictfamilia",dict(familia))
        json = dumps(familia.to_dict(show = ['membros', 'membros.contas','membros.contas.pagamentos']), cls = DecimalEncoder, indent = 1)
        print(json)
