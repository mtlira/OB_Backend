from decimal import Decimal
from model.business.classes_negocio import Usuario, Familia, Conta, Movimentacao
from setup import db
from sqlalchemy import select, and_, or_

def serialize(row, table):
    dict = {}
    for i in range(0,len(row)):
        dict[table.c.keys()[i]] = row[i]
    return dict

class DAO:
    def cadastroExiste(ficha):
        consulta = db.session.query(Usuario).filter(Usuario.c.email == ficha['email'] or Usuario.c.cpf == ficha['cpf']).all()
        if len(consulta) != 0: return True
        else: return False

    def persistirCadastro(ficha):
        cadastro = Usuario(ficha['nome'],ficha['cpf'],ficha['endereco'],ficha['telefone'],ficha['email'],ficha['senha'])
        db.session.add(cadastro)
        db.session.commit()
        del cadastro

    def getUsuario(email):
        consulta = db.session.query(Usuario).filter(Usuario.c.email == email).all()
        if len(consulta) == 0: return None
        return consulta[0]

    def contaExiste(id_banco, cpf):
        existe = False
        usuario = db.session.query(Usuario).join(Conta).filter(Usuario.c.cpf == cpf and Conta.c.id_banco == id_banco).all()

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
        id_usuario = db.session.query(Usuario).filter(Usuario.c.cpf == json['cpf_usuario']).one().id_usuario
        conta = Conta(json['id_banco'], id_usuario, json['agencia'], json['cc'])
        db.session.add(conta)
        db.session.commit()
        del conta

    def familiaExiste(id):
        if db.session.query(Familia).filter(Familia.c.id_familia == id).one_or_none() != None:
            return True
        return False
    #def getFamilia():
    #    with open('login_info.txt') as file:
    #        idLogin = file.readlines()[0].split()[1]
    #    id_familia = db.session.query(Usuario.id_familia).filter(Usuario.id_usuario == idLogin).one()[0]
    #    return id_familia

    def getFamilia(id, servico):
        if servico == "login" or servico == "entrar_familia":
            return db.session.query(Familia).filter(Familia.c.id_familia == id).one_or_none()
        elif servico == "centralizar":
            query = db.session.query(Familia).join(Usuario).filter(Usuario.c.id_usuario == id).one_or_none()
            return serialize(query, Familia) if query != None else None
        else:
            return None

    def persistirFamilia(id, nome, senha):
        with open('login_info.txt') as file:
            idLogin = file.readlines()[0].split()[1]
        db.session.add(Familia(id, nome, senha))
        db.session.query(Usuario).filter(Usuario.c.id_usuario == idLogin).update({"id_familia": id}, synchronize_session = False)
        db.session.commit()

    def isInFamilia():
        with open('login_info.txt') as file:
            idLogin = file.readlines()[0].split()[1]
        id_familia = db.session.query(Usuario.c.id_familia).filter(Usuario.c.id_usuario == idLogin).one()[0]
        if id_familia == None:
            return False
        return True         

    def persistirMembroFamilia(id):
        with open('login_info.txt') as file:
            idLogin = file.readlines()[0].split()[1]
        db.session.query(Usuario).filter(Usuario.c.id_usuario == idLogin).update({"id_familia": id}, synchronize_session = False)
        db.session.commit()

    def getMembros(idFamilia):
        membros = []
        query = db.session.query(Usuario).join(Familia).filter(Usuario.c.id_familia == idFamilia).all()
        for usuario in query: membros.append(serialize(usuario, Usuario))
        return membros

    def getContas(id_usuario):
        contas = []
        query = db.session.query(Conta).filter(Conta.c.id_usuario == id_usuario)
        for conta in query: contas.append(serialize(conta, Conta))
        return contas

    def getMovimentacoes(id_banco, id_usuario, tipo):
        movimentacoes = []
        print(id_banco,Movimentacao.c.id_banco_origem,id_usuario, Movimentacao.c.id_usuario_origem)
        print(id_banco,Movimentacao.c.id_banco_destino,id_usuario, Movimentacao.c.id_usuario_destino)
        if tipo == "pagamento": 
            query = db.session.query(Movimentacao).filter(
                or_(
                    and_(Movimentacao.c.id_banco_origem == id_banco, Movimentacao.c.id_usuario_origem == id_usuario),
                    and_(Movimentacao.c.id_banco_destino == id_banco, Movimentacao.c.id_usuario_destino == id_usuario)
                )
            )
        #if tipo == "recebimento": 
            #query = db.session.query(Movimentacao).filter(Movimentacao.c.id_banco_destino == id_banco and Movimentacao.c.id_usuario_destino == id_usuario)
        for movimentacao in query: movimentacoes.append(serialize(movimentacao, Movimentacao))
        return movimentacoes