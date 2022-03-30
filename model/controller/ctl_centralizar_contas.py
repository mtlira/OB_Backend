from model.DAO import DAO
from decimal import Decimal

class CTL_CentralizarContas:
    def centralizar(json):
        
        idLogin = json['id_login']

        #Familia
        familia = DAO.getFamilia(idLogin, "centralizar")
        dict = familia if familia != None else {'id_familia':'None'}
        dict['saldo_cc'] = Decimal(0.00)
        dict['saldo_pp'] = Decimal(0.00)

        #Usuario
        dict['membros'] = DAO.getMembros(familia['id_familia']) if familia != None else [DAO.getUsuario(idLogin, "idLogin")]

        #Contas
        for membro in dict['membros']:
            membro['saldo_cc'] = Decimal(0.00)
            membro['saldo_pp'] = Decimal(0.00)
            membro['contas'] = DAO.getContas(membro['id_usuario'])
            
            #Movimentacoes
            #print('#####contas####\n',membro['contas'])
            for conta in membro['contas']:
                conta['movimentacoes'] = DAO.getMovimentacoes(conta['id_banco'], conta['id_usuario'], "pagamento")
                membro['saldo_cc'] += conta['saldo_cc']
                membro['saldo_pp'] += conta['saldo_pp']
                #conta['recebimentos'] = DAO.getMovimentacoes(conta['id_banco'], conta['id_usuario'], "recebimento")
                #print('###movimentacoes###',conta['id_banco'],conta['id_usuario'],conta['movimentacoes'])
            dict['saldo_cc'] += membro['saldo_cc']
            dict['saldo_pp'] += membro['saldo_pp']

        #print(dict)
        return dict,201
