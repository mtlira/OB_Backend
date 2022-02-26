from model.dao.DAO import DAO
from global_variables import cpfLogin
from model.business.classes_negocio import Usuario

class CTL_AddContaBancaria: #Ajustar retornos!!
    def validarConta(id, ag, cc):
        global cpfLogin
        #"OpenBanking.getConta(id, ag, cc)" (Implementar funcionalidade da app basica)
        conta = { #JSON obtido da app basica
            "id_banco": 567,
            "cpf_usuario": 999,
            "agencia": 300,
            "cc": 456,
            "saldo_cc": 100,
            "saldo_pp": 5000
        }
        if cpfLogin != conta['cpf_usuario']:
            return '3', 405

        # Verifica se (id, ag, cc) da conta estao corretos
        elif conta == None or id != conta['id_banco'] or ag != conta['agencia'] or cc != conta['cc']:
            return '4', 405

        elif DAO.contaExiste(id):
                return '2', 405

        else:
            #OpenBanking.compartilharDados() (Implementar na app basica)
            DAO.persistirConta(conta)
            return '1', 200

def main_adicionar_conta(json):
    # 1 - frontend manda id, ag e cc do banco preenchidos pelo usuario
    #id = 987
    #ag = 123
    #cc = 456

    # 2 - chama validarConta do CTL
    contaAdicionada = CTL_AddContaBancaria.validarConta(json['id_banco'], json['agencia'], json['cc'])
    if contaAdicionada:
        print("Conta adicionada com sucesso")
    else:
        print("Nao foi possivel adicionar a conta: dados incorretos, a conta esta vinculada a outro CPF ou a conta ja existe.")

#Código de resultados:
#Sucesso:
#   1 - Conta adicionada com sucesso
#Falhas:
#   2 - Conta já foi adicionada ao aplicativo
#   3 - Conta vinculada a outro CPF
#   4 - Dados incorretos / Conta nao encontrada

if __name__ == '__main__':
    main_adicionar_conta()