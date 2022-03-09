from model.DAO import DAO

from flask import json
from setup import app

class CTL_CriarFamilia:
    def criarFamilia(data):
        if DAO.isInFamilia() is not None:
            print("Voce ja possui uma familia")
            # return '', 405
            
            message = {
                "mensagem": "JA_POSSUI_FAMILIA",
                "idFamilia": DAO.isInFamilia()
            }

            response = app.response_class(
                response=json.dumps(message),
                status=200,
                mimetype='application/json'
            )
            
            return response, 405

        elif DAO.familiaExiste(data['idFamilia']):
            print("Esse id ja é de uma familia")
            # return '', 405

            message = {
                "mensagem": "ID_NAO_DISPONIVEL"
            }

            response = app.response_class(
                response=json.dumps(message),
                status=200,
                mimetype='application/json'
            )
            
            return response, 405

        else:
            DAO.persistirFamilia(data['idFamilia'], data['nomeFamilia'], data['senhaFamilia'])
            print("Famiia criada com sucesso")
            # return '', 201

            message = {
                "mensagem": "OK",
                "idFamilia": data['idFamilia']
            }

            response = app.response_class(
                response=json.dumps(message),
                status=200,
                mimetype='application/json'
            )
            
            return response, 201