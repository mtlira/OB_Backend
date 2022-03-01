from model.DAO import DAO
class CTL_CriarFamilia:
    def criarFamilia(json):
        if DAO.isInFamilia():
            print("Voce ja possui uma familia")
            return '', 405
        elif DAO.familiaExiste(json['id_familia']):
            print("Esse id ja é de uma familia")
            return '', 405
        else:
            DAO.persistirFamilia(json['id_familia'], json['nome'], json['senha'])
            print("Famiia criada com sucesso")
            return '', 201