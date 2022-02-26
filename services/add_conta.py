from model.dao.DAO import DAO
from global_variables import cpfLogin
from model.business.classes_negocio import Usuario

class CTL_AddContaBancaria:
    def validarConta(id, ag, cc):
        global cpfLogin
        #"OpenBanking.getConta(id, ag, cc)" (Implementar funcionalidade da app básica)
        conta = { #JSON obtido da app basica
            "id_banco": 111,
            "cpf_usuario": 12345678900,
            "agencia": 120,
            "cc": 456,
            "saldo_cc": 100,
            "saldo_pp": 5000
        }
        # Verifica se (id, ag, cc) da conta estao corretos e se o cpf da conta eh o mesmo do usuario logado
        if conta == None or id != conta['id_banco'] or ag != conta['agencia'] or cc != conta['cc'] or cpfLogin != conta['cpf_usuario']:
            return False
        else:
            if DAO.contaExiste(id, cpfLogin):
                return False
            else:
                #OpenBanking.compartilharDados() (Implementar na app basica)
                DAO.persistirConta(conta)
                return True

def main_adicionar_conta():
    # 1 - frontend manda id, ag e cc do banco preenchidos pelo usuario
    id = 987
    ag = 123
    cc = 456

    # 2 - chama validarConta do CTL
    contaAdicionada = CTL_AddContaBancaria.validarConta(id, ag, cc)
    if contaAdicionada:
        print("Conta adicionada com sucesso")
    else:
        print("Nao foi possivel adicionar a conta: dados incorretos, a conta esta vinculada a outro CPF ou a conta ja existe.")

if __name__ == '__main__':
    main_adicionar_conta()