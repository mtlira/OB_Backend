from model.dao.DAO import DAO
from global_variables import idLogin, cpfLogin
#from classes_negocio import Usuario

class CTL_login:
    def validarAcesso(email, senha):
        # 3 - Puxa a senha do DB p/ verificar se: i) existe; ii) esta correta
        usuario = DAO.getUsuario(email)
        if senha == None or usuario.senha != senha:
            return False
        else:
            global idLogin
            idLogin = usuario.id_usuario
            cpfLogin = usuario.cpf
            return True

def main_login():
    # 1 - Usuario fornece dados de email e senha no front end
    # Implementar depois no front end
    email = "joaofreitas@gmail.com"
    senha = "1234"

    # 2 - Chama validarAcesso do controlador
    loginCorreto = CTL_login.validarAcesso(email, senha)
    if loginCorreto:
        print("Redirecionar para pagina Home") # FRONT END
    else:
        print("Email e/ou senha incorretos") # Remover depois. Essa mensagem sera mostrada na tela (FRONT-END)

if __name__ == '__main__':
    main_login()

