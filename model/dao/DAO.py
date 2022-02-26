from model.business.classes_negocio import Usuario, Conta
from setup import db

class DAO:
    def cadastroExiste(ficha):
        consulta = db.session.query(Usuario).filter(Usuario.email == ficha['email'] or Usuario.cpf == ficha['cpf']).all()
        if len(consulta) != 0: return True
        else: return False

    def persistirCadastro(ficha):
        cadastro = Usuario(ficha['nome'],ficha['cpf'],ficha['endereco'],ficha['telefone'],ficha['email'],ficha['senha'])
        db.session.add(cadastro)
        db.session.commit()
        del cadastro

    def getUsuario(email):
        consulta = db.session.query(Usuario).filter(Usuario.email == email).all()
        if len(consulta) == 0: return None
        return consulta[0]

    def contaExiste(id_banco):
        if len(db.session.query(Usuario, Conta).filter(Usuario.id_usuario == Conta.id_usuario and Conta.id_banco == id_banco).one()) == 0:
            return False
        else: 
            return True

    def persistirConta(json):
        id_usuario = db.session.query(Usuario).filter(Usuario.cpf == json['cpf_usuario']).all()[0].id_usuario
        conta = Conta(json['id_banco'], id_usuario, json['agencia'], json['cc'])
        db.session.add(conta)
        db.session.commit()
        del conta