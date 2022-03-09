from model.DAO import DAO

from flask import json
from setup import app

class CTL_EntrarFamilia:
    def entrarFamilia(data):
        if DAO.isInFamilia() is not None:
            print("Voce ja esta em uma familia")
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

        else:
            familia = DAO.getFamilia(data['idFamilia'])
            if familia == None:
                print("Dados incorretos ou a familia nao existe")
                # return '', 405
            
                message = {
                    "mensagem": "INC_OU_NEX"
                }

                response = app.response_class(
                    response=json.dumps(message),
                    status=200,
                    mimetype='application/json'
                )
            
                return response, 405
                
            elif familia.senha != data['senhaFamilia']:
                print("Senha incorreta")
                # return '', 405
                
                message = {
                    "mensagem": "SENHA_INCORRETA"
                }

                response = app.response_class(
                    response=json.dumps(message),
                    status=200,
                    mimetype='application/json'
                )
            
                return response, 405
            else:
                DAO.persistirMembroFamilia(data['idFamilia'])
                print("Adicionado a familia com sucesso")
                # return '', 201

                message = {
                    "mensagem": "OK"
                }

                response = app.response_class(
                    response=json.dumps(message),
                    status=200,
                    mimetype='application/json'
                )
            
                return response, 201
            
