from model.DAO import DAO

class CTL_CriarFamilia:
    def temFamilia(id_usuario):
        if DAO.isInFamilia(id_usuario):
            print("Voce ja possui uma familia")
            return {"mensagem":"TRUE"}, 405
        else:
            print("Usuario nao possui familia")
            return {"mensagem":"FALSE"}, 405

    def criarFamilia(json):
        if DAO.familiaExiste(json['id_familia']):
            print("Esse id ja é de uma familia")
            return {"mensagem":"ID_NAO_DISPONIVEL"}, 405
        else:
            DAO.persistirFamilia(json)
            print("Famiia criada com sucesso")
            return {"mensagem":"OK"}, 201
