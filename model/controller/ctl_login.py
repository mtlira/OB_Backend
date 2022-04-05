from model.DAO import DAO

class CTL_Login:
    def login(json):
        email = json['email']
        senha = json['senha']
        usuario = DAO.getUsuario(email, "email")
        if usuario == None or senha == None or usuario['senha'] != senha:
            print("Email e/ou senha incorretos")
            return {"mensagem":"DADOS_INCORRETOS"}, 401
        else:
            #file = open('login_info.txt','w')
            #file.write("idlogin {}\ncpfLogin {}".format(str(usuario['id_usuario']),str(usuario['cpf'])))
            #file.close()
            print("Redirecionar para pagina Home")
            return {"mensagem":"OK","id_login":"{}".format(usuario['id_usuario'])}, 201