from model.DAO import DAO
from model.controller.ctl_login import CTL_login
#from classes_negocio import Usuario

def main_login(json):
    # 1 - Usuario fornece dados de email e senha no front end
    # Implementar depois no front end
    #email = "joaofreitas@gmail.com"
    #senha = "1234"

    # 2 - Chama validarAcesso do controlador
    loginCorreto = CTL_login.validarAcesso(json['email'], json['senha'])
    if loginCorreto:
        print("Redirecionar para pagina Home") # FRONT END
        return {"mensagem":"OK"}, 201
    else:
        print("Email e/ou senha incorretos") # Remover depois. Essa mensagem sera mostrada na tela (FRONT-END)
        return {"mensagem":"DADOS_INCORRETOS"}, 401

if __name__ == '__main__':
    main_login()

