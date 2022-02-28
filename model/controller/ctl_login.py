from model.DAO import DAO
class CTL_login:
    def validarAcesso(email, senha):
        # 3 - Puxa a senha do DB p/ verificar se: i) existe; ii) esta correta
        usuario = DAO.getUsuario(email)
        if senha == None or usuario.senha != senha:
            return False
        else:
            file = open('login_info.txt','w')
            file.write("idlogin {}\ncpfLogin {}".format(str(usuario.id_usuario),str(usuario.cpf)))
            file.close()
            return True