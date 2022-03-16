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

@bp.route('/cadastrar', methods = ['POST'])
@cross_origin()
def API_cadastrar():
    data, httpCode = CTL_Cadastrar.cadastrar(request.get_json())
    return response(data, httpCode)

@bp.route('/login', methods = ['POST'])
@cross_origin()
def API_login():
    data, httpCode = CTL_Login.login(request.get_json())
    return response(data, httpCode)

@bp.route('/temfamilia', methods = ['GET'])
@cross_origin()
def API_tem_familia():
    data, httpCode = CTL_EntrarFamilia.temFamilia()
    return response(data, httpCode)

@bp.route('/addconta', methods = ['POST'])
@cross_origin()
def API_add_conta():
    data, httpCode = CTL_AddContaBancaria.addConta(request.get_json())
    return response(data, httpCode)

@bp.route('/criarfamilia', methods = ['POST'])
@cross_origin()
def API_criar_familia():
    data, httpCode = CTL_CriarFamilia.criarFamilia(request.get_json())
    return response(data, httpCode)

@bp.route('/entrarfamilia', methods = ['POST'])
@cross_origin()
def API_entrar_familia():
    data, httpCode = CTL_EntrarFamilia.entrarFamilia(request.get_json())
    return response(data, httpCode)

@bp.route('/centralizarcontas', methods = ['GET'])
@cross_origin()
def API_centralizar_contas():
    data, httpCode = CTL_CentralizarContas.centralizar()
    return response(data, httpCode)

# Links uteis: 
# https://docs.sqlalchemy.org/en/14/orm/query.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#simple-example
# https://auth0.com/blog/developing-restful-apis-with-python-and-flask/
