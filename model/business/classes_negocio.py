from setup import db

class Usuario(db.Model):
    id_usuario = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nome = db.Column(db.String(50),nullable = False)
    cpf = db.Column(db.Integer, nullable = False)
    endereco = db.Column(db.String(100), nullable = True)
    telefone = db.Column(db.Integer, nullable = True)
    email = db.Column(db.String(50), nullable = False)
    senha = db.Column(db.String(30), nullable = False)
    contas = db.relationship('Conta', backref = 'usuario', lazy = True)
    def __init__(self, nome, cpf, endereco, telefone, email, senha):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.senha = senha

class Familia:
    def __init__(self, id, senha, nome):
        self._id = id
        self._senha = senha
        self._nome = nome
        self._membros = []
    
    def adicionar(self,usuario):
        if usuario in self._membros: return False
        self._membros.append(usuario)
        return True

class Conta(db.Model): #CONSERTAR https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#simple-example
    id_banco = db.Column(db.Integer, primary_key = True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), primary_key = True)
    agencia = db.Column(db.Integer, nullable = False)
    cc = db.Column(db.Integer, nullable = False)
    saldo_cc = db.Column(db.Numeric, default = 0)
    saldo_pp = db.Column(db.Numeric, default = 0)
    def __init__(self, id_banco, id_usuario, agencia, cc):
        self.id_banco = id_banco
        self.id_usuario = id_usuario
        self.agencia = agencia
        self.cc = cc
        self.saldo_cc = 0
        self.saldo_pp = 0
        self.extrato = []

class Movimentacao:
    def __init__(self, origem, destino, data, descricao, valor):
        self._origem = origem
        self._destino = destino
        self._data = data
        self._descricao = descricao
        self._valor = valor

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
        if len(db.session.query(Usuario, Conta).filter(Usuario.id_usuario == Conta.id_usuario).one()) == 0:
            return False
        else: 
            return True

    def persistirConta(json):
        id_usuario = db.session.query(Usuario).filter(Usuario.cpf == json['cpf_usuario']).all()[0].id_usuario
        conta = Conta(json['id_banco'], id_usuario, json['agencia'], json['cc'])
        db.session.add(conta)
        db.session.commit()
        del conta