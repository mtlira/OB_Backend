from model.DAO import DAO
class CTL_TemFamilia:
    def temFamilia(login):
        idFamilia = DAO.isInFamilia(login)
        if idFamilia is not None:
            print("Voce ja possui uma familia")
            
        else:
            print("Ainda sem familia cadastrada")
        
        return idFamilia