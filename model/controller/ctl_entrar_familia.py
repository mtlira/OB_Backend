from model.DAO import DAO

class CTL_EntrarFamilia:
    def temFamilia():
        with open("login_info.txt",'r') as file:
            lines = file.readlines()
            idLogin = lines[0].split()[1]
        if DAO.isInFamilia(idLogin):
            print("Voce ja possui uma familia")
            return {"mensagem":"TRUE"}, 201
        else:
            print("Usuario nao possui familia")
            return {"mensagem":"FALSE"}, 201

    def entrarFamilia(json):
        if DAO.isInFamilia() is not None:
            print("Voce ja esta em uma familia")
            return {"mensagem":"JA_POSSUI_FAMILIA"}, 405
        else:
            familia = DAO.getFamilia(json['id_familia'], "entrar_familia")
            if familia == None:
                print("Dados incorretos ou a familia nao existe")
                return {"mensagem":"INC_OU_NEX"}, 405
            elif familia['senha'] != json['senha']:
                print("Senha incorreta")
                return {"mensagem":"SENHA_INCORRETA"}, 405
            else:
                DAO.persistirMembroFamilia(json['id_familia'])
                print("Adicionado a familia com sucesso")
                return {"mensagem":"OK"}, 201
            
