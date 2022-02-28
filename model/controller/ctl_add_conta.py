from model.DAO import DAO
from global_variables import cpfLogin

class CTL_AddContaBancaria: #Ajustar retornos!!
    def validarConta(id, ag, cc):
        #"OpenBanking.getConta(id, ag, cc)" (Implementar funcionalidade da app basica)
        conta = { #JSON obtido da app basica
            "id_banco": "567",
            "cpf_usuario": "999",
            "agencia": "300",
            "cc": "456",
            "saldo_cc": "100",
            "saldo_pp": "5000"
        }

        with open("login_info.txt",'r') as file:
            lines = file.readlines()
            idLogin = lines[0].split()[1]
            cpfLogin = lines[1].split()[1]
        if str(cpfLogin) != conta['cpf_usuario']:
            return 3

        # Verifica se (id, ag, cc) da conta estao corretos
        elif conta == None or id != conta['id_banco'] or ag != conta['agencia'] or cc != conta['cc']:
            return 4

        elif DAO.contaExiste(id, cpfLogin):
                return 2

        else:
            #OpenBanking.compartilharDados() (Implementar na app basica)
            DAO.persistirConta(conta)
            return 1

#Código de resultados:
#Sucesso:
#   1 - Conta adicionada com sucesso
#Falhas:
#   2 - Conta já foi adicionada ao aplicativo
#   3 - Conta vinculada a outro CPF
#   4 - Dados incorretos / Conta nao encontrada
