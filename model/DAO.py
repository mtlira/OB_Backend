from decimal import Decimal
from model.business.classes_negocio import Usuario, Familia, Conta, Movimentacao
from app import db
from sqlalchemy import insert, and_, or_

def serialize(row, table):
    dict = {}
    for i in range(0,len(row)):
        dict[table.c.keys()[i]] = row[i]
    return dict

class DAO:
    def cadastroExiste(ficha):
        consulta = db.session.query(Usuario).filter(or_(Usuario.c.email == ficha['email'], Usuario.c.cpf == ficha['cpf'])).all()
        if len(consulta) != 0: return True
        else: return False

    def persistirCadastro(ficha):
        stmt = insert(Usuario).values(
            nome = ficha['nome'],
            cpf = ficha['cpf'],
            endereco = ficha['endereco'],
            telefone = ficha['telefone'],
            email = ficha['email'],
            senha = ficha['senha']
            )
        
        with db.engine.connect() as conn:
            conn.execute(stmt)
            #conn.commit()

    def getUsuario(key, key_type):
        query = None
        if key_type == "email": 
            query = db.session.query(Usuario).filter(Usuario.c.email == key).one_or_none()
        if key_type == "idLogin":
            query = db.session.query(Usuario).filter(Usuario.c.id_usuario == key).one_or_none()
        
        if query == None: return None
        return serialize(query, Usuario)

    def contaExiste(id_banco, cpf):
        query = db.session.query(Usuario).join(Conta).filter(and_(Usuario.c.cpf == cpf,Conta.c.id_banco == id_banco)).all()
        if len(query) == 0: return False
        else: return True

    def persistirConta(json):
        idUsuario = db.session.query(Usuario.c.id_usuario).filter(Usuario.c.cpf == json['cpf']).one()[0]
        stmt = insert(Conta).values(
            id_banco = json['id_banco'],
            id_usuario = idUsuario,
            token = json['token']
            #agencia = json['agencia'],
            #cc = json['cc'],
            #saldo_cc = json['saldo_cc'],
            #saldo_pp = json['saldo_pp']
            )
        with db.engine.connect() as conn:
            conn.execute(stmt)
            #conn.commit()

    def familiaExiste(id):
        if db.session.query(Familia).filter(Familia.c.id_familia == id).one_or_none() != None:
            return True
        return False

    def getFamilia(id, servico):
        if servico == "login" or servico == "entrar_familia":
            query = db.session.query(Familia).filter(Familia.c.id_familia == str(id)).one_or_none()
            if query == None: return None
            return serialize(query, Familia)

        elif servico == "centralizar":
            query = db.session.query(Familia.c.id_familia,Familia.c.nome).join(Usuario).filter(Usuario.c.id_usuario == int(id)).one_or_none()
            if query == None: return None
            return serialize(query, Familia) if query != None else None
        else:
            return None

    def persistirFamilia(json):
        stmt = insert(Familia).values(
            id_familia = json['id_familia'],
            nome = json['nome'],
            senha = json['senha']
            )
        with db.engine.connect() as conn:
            conn.execute(stmt)
            #conn.commit()

        db.session.query(Usuario).filter(Usuario.c.id_usuario == json['id_login']).update({"id_familia": json['id_familia']}, synchronize_session = False)
        db.session.commit()

    def isInFamilia(id_usuario):
        #with open('login_info.txt') as file:
            #idLogin = file.readlines()[0].split()[1]
        id_familia = db.session.query(Usuario.c.id_familia).filter(Usuario.c.id_usuario == int(id_usuario)).one()[0]
        if id_familia == None:
            return False
        return True         

    def persistirMembroFamilia(json):
        idLogin = json['id_login']
        idFamilia = json['id_familia']
        db.session.query(Usuario).filter(Usuario.c.id_usuario == idLogin).update({"id_familia": idFamilia}, synchronize_session = False)
        db.session.commit()

    def getMembros(idFamilia):
        membros = []
        if idFamilia != None:
            query = db.session.query(Usuario.c.id_usuario, Usuario.c.id_familia, Usuario.c.nome).join(Familia).filter(Usuario.c.id_familia == idFamilia).all()
            for usuario in query:
                membros.append(serialize(usuario, Usuario))
        return membros

    def getContas(id_usuario):
        contas = []
        query = db.session.query(Conta).filter(Conta.c.id_usuario == id_usuario)
        for conta in query: contas.append(serialize(conta, Conta))
        return contas

    def getMovimentacoes(id_banco, id_usuario, tipo):
        movimentacoes = []
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
    
    def updateToken(id_banco, id_login, token):
        db.session.query(Conta).filter(Conta.c.id_usuario == id_login).update({"token": token}, synchronize_session = False)
        db.session.commit()