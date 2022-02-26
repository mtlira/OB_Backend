from flask import request, make_response, abort
from services.cadastro import main_cadastro
from flask_cors import cross_origin
from setup import app, db

@app.route('/')
def home():
    print("oi")

@app.route('/cadastrar', methods = ['POST'])
@cross_origin()#headers = ["Content-Type"], methods = ['POST'], automatic_options = True)
def API_cadastrar():
    # Dados cadastro: nome completo, nascimento, cpf, endereco, telefone, email, senha
    print("teste5")
    main_cadastro(request.get_json())
    return '', 204

#def API_cadastrar():
    #print("entrou")
    #handle_result = {'result': True, 'msg': 'success'}
    #try:
    #    origin = request.environ['http://127.0.0.1']
    #except KeyError:
     #   origin = None

    #if origin and origin.find('127.0.0.1') > -1:
    #    main_cadastro(request.get_json())
    #    resp = make_response(str(handle_result))
    #    resp.headers['Content-Type'] = 'application/json'

    #    h = resp.headers
    #    h['Access-Control-Allow-Origin'] = 'http://127.0.0.1:3000'
    #    h['Access-Control-Allow-Methods'] = 'GET, POST, PATCH, PUT, DELETE, OPTIONS'
    #    h['Access-Control-Allow-Headers'] = 'Content-Type'

    #    resp.headers = h
    #    return resp
    
    #return abort(403)

if __name__ == "__main__":        
    db.create_all()
    app.run(host='0.0.0.0', port=5000, debug = True)

# Links uteis: 
# https://docs.sqlalchemy.org/en/14/orm/query.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#simple-example
# https://auth0.com/blog/developing-restful-apis-with-python-and-flask/
