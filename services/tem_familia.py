from model.DAO import DAO
from model.controller.ctl_tem_familia import CTL_TemFamilia

from flask import json
from setup import app

def main_tem_familia(data):
    jaTemFamilia = CTL_TemFamilia.temFamilia(data['login'])
    if jaTemFamilia is not None:
        print("Redirecionar para pagina home de familia")

        data = {
            "mensagem": "tem_familia",
            "idFamilia": jaTemFamilia
        }

        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        
        return response, 202

    else:
        print("Redirecionar para criar/entrar família")
        
        data = {
            "mensagem": "sem_familia",
            "idFamilia": False
        }

        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        
        return response, 401

if __name__ == '__main__':
    main_tem_familia()

