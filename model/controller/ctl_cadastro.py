from model.dao.DAO import DAO
class CTL_Cadastro:
    # 3 - Verifica-se se o email e cpf de cadastro ja existem na DB
    def cadastrar(ficha):
        if DAO.cadastroExiste(ficha):
            return False
        else: 
            DAO.persistirCadastro(ficha)
            return True