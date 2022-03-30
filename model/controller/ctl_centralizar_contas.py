from model.DAO import DAO
from decimal import Decimal

class CTL_CentralizarContas:
    def centralizar():
        #rowtodict = lambda r: {c.name: str(getattr(r, c.name)) for c in r.__table__.columns}
        with open('login_info.txt') as file:
            info = file.readlines()
            idLogin = info[0].split()[1]
            cpfLogin = info[1].split()[1]
        
        #Familia
        familia = DAO.getFamilia(idLogin, "centralizar")
        family_dict = familia if familia != None else {'id_familia':'None'}
        family_dict['saldo_cc'] = Decimal(0.00)
        family_dict['saldo_pp'] = Decimal(0.00)

        #Usuario
        family_dict['membros'] = DAO.getMembros(familia['id_familia']) if familia != None else [DAO.getUsuario(idLogin, "idLogin")]

        #Contas
        for membro in family_dict['membros']:
            membro['saldo_cc'] = Decimal(0.00)
            membro['saldo_pp'] = Decimal(0.00)
            membro['contas'] = DAO.getContas(membro['id_usuario'])
            
            #Movimentacoes
            #print('#####contas####\n',membro['contas'])
            for conta in membro['contas']:
                conta['movimentacoes'] = DAO.getMovimentacoes(conta['id_banco'], conta['id_usuario'], "pagamento")
                membro['saldo_cc'] += Decimal(conta['saldo_cc'])
                membro['saldo_pp'] += Decimal(conta['saldo_pp'])
                #conta['recebimentos'] = DAO.getMovimentacoes(conta['id_banco'], conta['id_usuario'], "recebimento")
                #print('###movimentacoes###',conta['id_banco'],conta['id_usuario'],conta['movimentacoes'])
            family_dict['saldo_cc'] += membro['saldo_cc']
            family_dict['saldo_pp'] += membro['saldo_pp']

        print ('>>>>>>>>>>>>>>>>>>>>>')
        # print (family_dict["membros"][0]["contas"])
        return family_dict,201
