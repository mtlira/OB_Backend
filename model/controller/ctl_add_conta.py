from model.DAO import DAO
from global_variables import cpfLogin

class CTL_AddContaBancaria: #Ajustar retornos!!
    def addConta(json):
        #Redireciona pra app básica pra criar o consentimento
        #Passar nome e cpf
        id = json['id_banco']
        token = json['token']
        #ag = json['agencia'] #tirar
        #cc = json['cc'] #tirar
        idLogin = json['id_login'] # Vem do front da inovadora
        cpf = json['cpf']

        #Pedro Cunha
        conta1 = { #JSON obtido da app basica
            "id_banco": "567",
            "cpf_usuario": "999",
            "agencia": "300",
            "cc": "456",
            "saldo_cc": "10",
            "saldo_pp": "20"
        }

        #Joao Cunha
        conta2 = { #JSON obtido da app basica
            "id_banco": "567",
            "cpf_usuario": "1000",
            "agencia": "301",
            "cc": "456",
            "saldo_cc": "100",
            "saldo_pp": "200"
        }

        #Abelardo
        conta3 = { #JSON obtido da app basica
            "id_banco": "1",
            "cpf_usuario": "111",
            "agencia": "2",
            "cc": "3",
            "saldo_cc": "10000",
            "saldo_pp": "15000"
        }

        #Abelardo
        conta4 = { #JSON obtido da app basica
            "id_banco": "2",
            "cpf_usuario": "111",
            "agencia": "3",
            "cc": "4",
            "saldo_cc": "100",
            "saldo_pp": "5000"
        }

        #try:
        #    if json['teste'] == "1": conta = conta1
        #    if json['teste'] == "2": conta = conta2
        #    if json['teste'] == "3": conta = conta3
        #    if json['teste'] == "4": conta = conta4
        
        #except KeyError:
        #    conta = conta1

        usuario = DAO.getUsuario(idLogin, "idLogin")
        
        #if str(usuario['cpf']) != conta['cpf_usuario']:
        #    print("Conta vinculada a outro CPF")
        #    return {"mensagem":"OUTRO_CPF"}, 405

        # Verifica se (id, ag, cc) da conta estao corretos
        # Acho que nao sera mais necessario
        #elif conta == None or id != conta['id_banco'] or ag != conta['agencia'] or cc != conta['cc']:
        #    print("Dados incorretos / Conta nao encontrada")
        #    return {"mensagem":"NAO_ENCONTRADA"}, 405

        #TODO: se a conta existe, update. Se não, criar nova linha
        if DAO.contaExiste(id, usuario['cpf']):
            DAO.updateToken(id, idLogin, token)
            print("Conta ja foi adicionada. Token update")
            return {"mensagem":"JA_ADICIONADA"}, 405

        else:
            #OpenBanking.compartilharDados() (Implementar na app basica)
            DAO.persistirConta(json)
            print("Conta adicionada com sucesso")
            return {"mensagem":"OK"}, 201

#Código de resultados:
#Sucesso:
#   1 - Conta adicionada com sucesso
#Falhas:
#   2 - Conta já foi adicionada ao aplicativo
#   3 - Conta vinculada a outro CPF
#   4 - Dados incorretos / Conta nao encontrada
