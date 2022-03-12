from model.DAO import DAO
from json import dumps, JSONEncoder

from sqlalchemy.ext.declarative import DeclarativeMeta

from decimal import Decimal


class CTL_CentralizarContas:
    def centralizar():
        #rowtodict = lambda r: {c.name: str(getattr(r, c.name)) for c in r.__table__.columns}
        with open('login_info.txt') as file:
            info = file.readlines()
            idLogin = info[0].split()[1]
            emailLogin = info[1].split()[1]
        
        #Familia
        dict = DAO.getFamilia(idLogin, "centralizar")

        #Usuario
        #membros = DAO.getMembros(dict['id_familia'])
        dict['saldo_cc'] = Decimal(0.00)
        dict['saldo_pp'] = Decimal(0.00)
        dict['membros'] = DAO.getMembros(dict['id_familia'])
        #print(dict)

        #Contas
        for membro in dict['membros']:
            membro['contas'] = DAO.getContas(membro['id_usuario'])
            membro['saldo_cc'] = Decimal(0.00)
            membro['saldo_pp'] = Decimal(0.00)
            
            #Movimentacoes
            print('#####contas####\n',membro['contas'])
            for conta in membro['contas']:
                conta['pagamentos'] = DAO.getMovimentacoes(conta['id_banco'], conta['id_usuario'], "pagamento")
                membro['saldo_cc'] += conta['saldo_cc']
                membro['saldo_pp'] += conta['saldo_pp']
                #conta['recebimentos'] = DAO.getMovimentacoes(conta['id_banco'], conta['id_usuario'], "recebimento")
                print('###pagamentos###',conta['id_banco'],conta['id_usuario'],conta['pagamentos'])
            dict['saldo_cc'] += membro['saldo_cc']
            dict['saldo_pp'] += membro['saldo_pp']

        print(dict)
        return '',201
