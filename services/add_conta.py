from model.controller.ctl_add_conta import CTL_AddContaBancaria

def main_adicionar_conta(json):
    # 1 - frontend manda id, ag e cc do banco preenchidos pelo usuario
    #id = 987
    #ag = 123
    #cc = 456

    # 2 - chama validarConta do CTL
    status = CTL_AddContaBancaria.validarConta(json['id_banco'], json['agencia'], json['cc'])
    if status == 1: 
        print("Conta adicionada com sucesso")
        return '', 201
    elif status == 2:
        print("Conta ja foi adicionada")
        return '', 405
    elif status == 3:
        print("Conta vinculada a outro CPF")
        return '',405
    else:
        print("Dados incorretos / Conta nao encontrada")
        return '', 405

#Código de resultados:
#Sucesso:
#   1 - Conta adicionada com sucesso
#Falhas:
#   2 - Conta já foi adicionada ao aplicativo
#   3 - Conta vinculada a outro CPF
#   4 - Dados incorretos / Conta nao encontrada

if __name__ == '__main__':
    main_adicionar_conta()