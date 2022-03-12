from model.DAO import DAO
class CTL_Cadastrar:
    def cadastrar(ficha):
        if DAO.cadastroExiste(ficha):
            print("CPF ja cadastrado.")
            return {"mensagem":"JA_CADASTRADO"}, 405
        else: 
            DAO.persistirCadastro(ficha)
            print("Cadastro realizado com sucesso")
            return {"mensagem":"OK"}, 201