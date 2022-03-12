from flask import request
from services.cadastro import main_cadastro
from services.login import main_login
from services.add_conta import main_adicionar_conta
from model.controller.ctl_criar_familia import CTL_CriarFamilia
from model.controller.ctl_entrar_familia import CTL_EntrarFamilia
from model.controller.ctl_centralizar_contas import CTL_CentralizarContas
from flask_cors import cross_origin
from setup import app, db


@app.route('/cadastrar', methods = ['POST'])
@cross_origin()
def API_cadastrar():
    # Dados cadastro: nome completo, nascimento, cpf, endereco, telefone, email, senha
    return main_cadastro(request.get_json())

@app.route('/login', methods = ['POST'])
@cross_origin()
def API_login():
    return main_login(request.get_json())

@app.route('/addconta', methods = ['POST'])
@cross_origin()
def API_add_conta():
    return main_adicionar_conta(request.get_json())

@app.route('/criarfamilia', methods = ['POST'])
@cross_origin()
def API_criar_familia():
    return CTL_CriarFamilia.criarFamilia(request.get_json())

@app.route('/entrarfamilia', methods = ['POST'])
@cross_origin()
def API_entrar_familia():
    return CTL_EntrarFamilia.entrarFamilia(request.get_json())

@app.route('/centralizarcontas', methods = ['GET'])
@cross_origin()
def API_centralizar_contas():
    return CTL_CentralizarContas.centralizar()

if __name__ == "__main__":        
    db.create_all()
    app.run(debug = True)

# Links uteis: 
# https://docs.sqlalchemy.org/en/14/orm/query.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#simple-example
# https://auth0.com/blog/developing-restful-apis-with-python-and-flask/
