from model.DAO import DAO
from global_variables import cpfLogin

class CTL_AddContaBancaria: #Ajustar retornos!!
    def addConta(json):
        #Redireciona pra app básica pra criar o consentimento
        #Passar nome e cpf
        id = json['id_banco']
        ag = json['agencia']
        cc = json['cc']
        #"OpenBanking.getConta(id, ag, cc)" (Implementar funcionalidade da app basica)
        conta1 = { #JSON obtido da app basica
            "id_banco": "567",
            "cpf_usuario": "1000",
            "agencia": "301",
            "cc": "456",
            "saldo_cc": "100",
            "saldo_pp": "5000"
        }

        conta3 = { #JSON obtido da app basica
            "id_banco": "1",
            "cpf_usuario": "111",
            "agencia": "2",
            "cc": "3",
            "saldo_cc": "100",
            "saldo_pp": "5000"
        }

        conta4 = { #JSON obtido da app basica
            "id_banco": "2",
            "cpf_usuario": "111",
            "agencia": "3",
            "cc": "4",
            "saldo_cc": "100",
            "saldo_pp": "5000"
        }

        conta = conta4

        with open("login_info.txt",'r') as file:
            lines = file.readlines()
            idLogin = lines[0].split()[1]
            cpfLogin = lines[1].split()[1]
        
        if str(cpfLogin) != conta['cpf_usuario']:
            print("Conta vinculada a outro CPF")
            return {"mensagem":"OUTRO_CPF"}, 405

        # Verifica se (id, ag, cc) da conta estao corretos
        elif conta == None or id != conta['id_banco'] or ag != conta['agencia'] or cc != conta['cc']:
            print("Dados incorretos / Conta nao encontrada")
            return {"mensagem":"NAO_ENCONTRADA"}, 405

        elif DAO.contaExiste(id, cpfLogin):
            print("Conta ja foi adicionada")
            return {"mensagem":"JA_ADICIONADA"}, 405

        else:
            #OpenBanking.compartilharDados() (Implementar na app basica)
            DAO.persistirConta(conta)
            print("Conta adicionada com sucesso")
            return {"mensagem":"OK"}, 201

#Código de resultados:
#Sucesso:
#   1 - Conta adicionada com sucesso
#Falhas:
#   2 - Conta já foi adicionada ao aplicativo
#   3 - Conta vinculada a outro CPF
#   4 - Dados incorretos / Conta nao encontrada
