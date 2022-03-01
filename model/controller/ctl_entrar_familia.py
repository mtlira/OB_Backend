from model.DAO import DAO
class CTL_EntrarFamilia:
    def entrarFamilia(json):
        if DAO.isInFamilia():
            print("Voce ja esta em uma familia")
            return '', 405
        else:
            familia = DAO.getFamilia(json['id_familia'])
            if familia == None:
                print("Dados incorretos ou a familia nao existe")
                return '', 405
            elif familia.senha != json['senha']:
                print("Senha incorreta")
                return '', 405
            else:
                DAO.persistirMembroFamilia(json['id_familia'])
                print("Adicionado a familia com sucesso")
                return '', 201
            
