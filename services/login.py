from model.DAO import DAO
from model.controller.ctl_login import CTL_login

from flask import json
from setup import app

#from classes_negocio import Usuario

def main_login(data):
    # 1 - Usuario fornece dados de email e senha no front end
    # Implementar depois no front end
    #email = "joaofreitas@gmail.com"
    #senha = "1234"

    # 2 - Chama validarAcesso do controlador
    loginCorreto = CTL_login.validarAcesso(data['email'], data['senha'])
    if loginCorreto:
        print("Redirecionar para pagina Home. Login correto") # FRONT END
        # return '', 202

        data = {
            "mensagem": "OK"
        }

        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        
        return response, 202

    else:
        print("Email e/ou senha incorretos") # Remover depois. Essa mensagem sera mostrada na tela (FRONT-END)
        # return '', 401
        
        data = {
            "mensagem": "DADOS_INCORRETOS"
        }

        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        
        return response, 401

if __name__ == '__main__':
    main_login()

