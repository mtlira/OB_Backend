from model.business.classes_negocio import Usuario, Familia, Conta
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

    def contaExiste(id_banco, cpf):
        existe = False
        usuario = db.session.query(Usuario, Conta).join(Usuario.contas).filter(Usuario.cpf == cpf and Conta.id_banco == id_banco).all()

        #query = db.select(Usuario, Conta).join(Usuario.contas)
        #for conta in contas:
            #if conta.id_banco == id_banco and 
        #if usuario != None: print(usuario.nome, usuario.id_usuario, usuario.cpf)
        #else: print("Usuario None")
        #print(usuario[0])
        if len(usuario) == 0: return False
        else: return True
        #if len(db.session.query(Usuario, Conta).filter(Usuario.cpf == cpf and Usuario.id_usuario == Conta.id_usuario and Conta.id_banco == id_banco).one()) == 0:
        #    return False
        #else: 
        #    return True

    def persistirConta(json):
        id_usuario = db.session.query(Usuario).filter(Usuario.cpf == json['cpf_usuario']).one().id_usuario
        conta = Conta(json['id_banco'], id_usuario, json['agencia'], json['cc'])
        db.session.add(conta)
        db.session.commit()
        del conta

    def familiaExiste(id):
        if db.session.query(Familia).filter(Familia.id_familia == id).one_or_none() != None:
            return True
        return False
    #def getFamilia():
    #    with open('login_info.txt') as file:
    #        idLogin = file.readlines()[0].split()[1]
    #    id_familia = db.session.query(Usuario.id_familia).filter(Usuario.id_usuario == idLogin).one()[0]
    #    return id_familia

    def getFamilia(id, servico):
        if servico == "login":
            return db.session.query(Familia).filter(Familia.id_familia == id).one_or_none()
        elif servico == "centralizar":
            return db.session.query(Familia).join(Familia.membros).filter(Usuario.id_usuario == id).one_or_none()
        else:
            return None

    def persistirFamilia(id, nome, senha):
        with open('login_info.txt') as file:
            idLogin = file.readlines()[0].split()[1]
        db.session.add(Familia(id, nome, senha))
        db.session.query(Usuario).filter(Usuario.id_usuario == idLogin).update({"id_familia": id}, synchronize_session = False)
        db.session.commit()

    def isInFamilia():
        with open('login_info.txt') as file:
            idLogin = file.readlines()[0].split()[1]
        id_familia = db.session.query(Usuario.id_familia).filter(Usuario.id_usuario == idLogin).one()[0]
        if id_familia == None:
            return False
        return True         

    def persistirMembroFamilia(id):
        with open('login_info.txt') as file:
            idLogin = file.readlines()[0].split()[1]
        db.session.query(Usuario).filter(Usuario.id_usuario == idLogin).update({"id_familia": id}, synchronize_session = False)
        db.session.commit()