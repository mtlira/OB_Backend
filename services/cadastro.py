from model.controller.ctl_cadastro import CTL_Cadastro
def main_cadastro(ficha):
    # 1 - A ficha de cadastro é obtida do frontend
    # Dados cadastro: nome completo, nascimento, cpf, endereco, telefone, email, senha
    ### Implementar parte em que a ficha é obtida do frontend

    # 2 - Chama o metodo cadastrar de CTL_Cadastro
    cadastrou = CTL_Cadastro.cadastrar(ficha)
    if not cadastrou:
        print("CPF e/ou senha ja foram cadastrados.") # Remover depois. Essa mensagem sera mostrada na tela (front-end)
        return '', 405
    else:
        print("Cadastro realizado com sucesso") # Remover depois. Essa mensagem sera mostrada na tela (front-end)
        return '', 201

ficha = {
    "nome": "João Freitas",
    "nascimento": "01/01/1998",
    "cpf": 12345678900,
    "endereco": "Av Afranio Peixoto 100 ap 201 - SP",
    "telefone": 11987654321,
    "email": "joaofreitas@gmail.com",
    "senha": "1234"
    }

if __name__ == '__main__':
    main_cadastro(ficha)

