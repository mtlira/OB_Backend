from model.DAO import DAO
class CTL_CriarFamilia:
    def criarFamilia(json):
        if DAO.isInFamilia():
            print("Voce ja possui uma familia")
            return {"mensagem":"JA_POSSUI_FAMILIA"}, 405
        elif DAO.familiaExiste(json['id_familia']):
            print("Esse id ja é de uma familia")
            return {"mensagem":"ID_NAO_DISPONIVEL"}, 405
        else:
            DAO.persistirFamilia(json['id_familia'], json['nome'], json['senha'])
            print("Famiia criada com sucesso")
            return {"mensagem":"OK"}, 201