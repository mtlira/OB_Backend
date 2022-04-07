from model.DAO import DAO

class CTL_CriarFamilia:
    def criarFamilia(json):
        if DAO.familiaExiste(json['id_familia']):
            print("Esse id ja é de uma familia")
            return {"mensagem":"ID_NAO_DISPONIVEL"}, 405
        elif DAO.isInFamilia(json['id_login']):
            return {"mensagem":"JA_POSSUI_FAMILIA"}, 405
        else:
            DAO.persistirFamilia(json)
            print("Familia criada com sucesso")
            return {"mensagem":"OK"}, 201