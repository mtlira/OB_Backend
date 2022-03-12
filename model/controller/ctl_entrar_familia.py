from model.DAO import DAO
class CTL_EntrarFamilia:
    def entrarFamilia(json):
        if DAO.isInFamilia():
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
            
