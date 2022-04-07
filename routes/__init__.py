from model.controller.ctl_cadastrar import CTL_Cadastrar
from model.controller.ctl_login import CTL_Login
from model.controller.ctl_add_conta import CTL_AddContaBancaria
from model.controller.ctl_criar_familia import CTL_CriarFamilia
from model.controller.ctl_entrar_familia import CTL_EntrarFamilia
from model.controller.ctl_centralizar_contas import CTL_CentralizarContas
from flask_cors import cross_origin
from .blueprint import bp
from .response_handler import response
from flask import request
from config.env_load import SECRET_KEY
from json import dumps
# imports for PyJWT authentication
import jwt
from datetime import datetime, timedelta
from functools import wraps

# decorator for verifying the JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = str(request.headers['x-access-token'])
        
        # return 401 if token is not passed
        if not token:
            return response({"mensagem":"TOKEN_NAO_ADICIONADO"}, 401)

        try:
            #decoding the payload to fetch the stored details
            data = jwt.decode(token, SECRET_KEY, "HS256")
        except:
            return response({"mensagem":"TOKEN_INVALIDO"}, 401)
        #return the payload after login verified
        json = request.get_json()
        if json == None: json = {}
        json['id_login'] = data['id_login']

        return f(json, *args, **kwargs)
    return decorated

@bp.route('/cadastrar', methods = ['POST'])
@cross_origin()
def API_cadastrar():
    data, httpCode = CTL_Cadastrar.cadastrar(request.get_json())
    return response(data, httpCode)

@bp.route('/login', methods = ['POST'])
@cross_origin()
def API_login():
    data, httpCode = CTL_Login.login(request.get_json())
    if data['mensagem'] == "OK":
        data['exp'] = datetime.utcnow() + timedelta(minutes = 60)
        data.pop('mensagem',None)
        data = {"mensagem":"OK", "token":jwt.encode(data, SECRET_KEY)} # data inclui o token

        # Para testes
        import os
        with open(os.path.join(os.path.dirname(__file__), '..','test','jwt.txt'), 'w') as file:
            file.write(data['token'])

    return response(data, httpCode)

@bp.route('/addconta', methods = ['POST'])
@cross_origin()
@token_required
def API_add_conta(json):
    data, httpCode = CTL_AddContaBancaria.addConta(json)
    return response(data, httpCode)

@bp.route('/temfamilia', methods = ['GET'])
@cross_origin()
@token_required
def API_tem_familia(json):
    data, httpCode = CTL_EntrarFamilia.temFamilia(json)
    return response(data, httpCode)

@bp.route('/criarfamilia', methods = ['POST'])
@cross_origin()
@token_required
def API_criar_familia(json):
    data, httpCode = CTL_CriarFamilia.criarFamilia(json)
    return response(data, httpCode)

@bp.route('/entrarfamilia', methods = ['POST'])
@cross_origin()
@token_required
def API_entrar_familia(json):
    data, httpCode = CTL_EntrarFamilia.entrarFamilia(json)
    return response(data, httpCode)

@bp.route('/centralizarcontas', methods = ['GET'])
@cross_origin()
@token_required
def API_centralizar_contas(json):
    data, httpCode = CTL_CentralizarContas.centralizar(json)
    return response(data, httpCode)

@bp.route('/')
@cross_origin()
def home():
    return "<p>homepage</p>"

#@bp.route('/favicon.ico')
#@cross_origin()
#def favicon():
#    return "", 200

# Links uteis: 
# https://docs.sqlalchemy.org/en/14/orm/query.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#simple-example
# https://auth0.com/blog/developing-restful-apis-with-python-and-flask/
