from config.env_load import BASIC_APP_URL
from model.DAO import DAO
from decimal import Decimal
import requests
from json import dumps

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

            print('TESTE GETTOKEN')
            # Puxar contas do Open Banking
            # Para cada pessoa da familia, chamar /getcontas da basica
            # response: json com dados bancarios de cada membro
            # Para uma determinada conta: se consentimento for invalido, json tem mensagem de erro
            #TODO:getContas(token)

            #pegar token da DB para membro
            #token = DAO.getToken(membro['id_usuario'])
            #print("token getToken",token)
            #response = requests.get('https://backend-basica/get_conta', headers=headers, data = data)

            membro['contas'] = DAO.getContas(membro['id_usuario'])
            
            #Movimentacoes
            for conta in membro['contas']:
                headers = {'Content-Type': 'application/json'}
                token = DAO.getToken(conta['id_banco'], membro['id_usuario'])
                print("token getToken",token)
                payload = dumps({"token": token, "cpf": membro['cpf']})
                response_json = requests.get(BASIC_APP_URL+'/get_conta', headers=headers, data = payload).json()
                print(response_json)
                conta['saldo_cc'] = Decimal(response_json['data']['availableAmount_CHECKING'])
                conta['saldo_pp'] = Decimal(response_json['data']['availableAmount_SAVINGS'])
                conta['movimentacoes'] = DAO.getMovimentacoes(conta['id_banco'], conta['id_usuario'], "pagamento")
                membro['saldo_cc'] += conta['saldo_cc']
                membro['saldo_pp'] += conta['saldo_pp']
            dict['saldo_cc'] += membro['saldo_cc']
            dict['saldo_pp'] += membro['saldo_pp']

        #print(dict)
        return dict,201
