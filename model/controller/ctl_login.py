from model.DAO import DAO
from json import dumps #APAGAR
class CTL_login:
    def validarAcesso(email, senha):
        # 3 - Puxa a senha do DB p/ verificar se: i) existe; ii) esta correta
        usuario = DAO.getUsuario(email)

        #deletar depois
        #print(usuario.__dict__)
        #print(usuario.contas[0].__dict__,usuario.contas.__dict__)
        #print("state\n",usuario.__dict__['_sa_instance_state'].__dict__)
        #json = dumps(usuario.__dict__, default = lambda o:o.__dict__, indent = 1)
        #print(json)
        
        if usuario == None or senha == None or usuario.senha != senha:
            return False
        else:
            file = open('login_info.txt','w')
            file.write("idlogin {}\ncpfLogin {}".format(str(usuario.id_usuario),str(usuario.cpf)))
            file.close()
            return True