from model.DAO import DAO
class CTL_CriarFamilia:
    def criarFamilia(json):
        id_familia = DAO.getFamilia()
        if id_familia != None:
            print("Voce ja possui uma familia")
            return '', 405
        else:
            DAO.persistirFamilia(json['id_familia'], json['nome'], json['senha'])
            print("Famiia criada com sucesso")
            return '', 201