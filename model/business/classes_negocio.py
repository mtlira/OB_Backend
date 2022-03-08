from setup import db
from model.business.basemodel import BaseModel
from sqlalchemy import ForeignKeyConstraint, PrimaryKeyConstraint


class Usuario(BaseModel):
    id_usuario = db.Column(db.Integer, primary_key = True, autoincrement = True)
    id_familia = db.Column(db.String(15), db.ForeignKey('familia.id_familia'))
    nome = db.Column(db.String(50),nullable = False)
    cpf = db.Column(db.Integer, nullable = False)
    endereco = db.Column(db.String(100), nullable = True)
    telefone = db.Column(db.Integer, nullable = True)
    email = db.Column(db.String(50), nullable = False)
    senha = db.Column(db.String(30), nullable = False)
    contas = db.relationship('Conta', backref = 'usuario')
    saldo_cc = 0
    saldo_pp = 0
    saldo_total = 0
    #pagamentos = db.relationship("Movimentacao", primaryjoin = "Usuario.id_usuario == Movimentacao.id_usuario_origem", backref = "usuario_origem", foreign_keys = "[Movimentacao.id_usuario_origem]")
    #recebimentos = db.relationship("Movimentacao", primaryjoin = "Usuario.id_usuario == Movimentacao.id_usuario_destino", backref = "usuario_destino", foreign_keys = "[Movimentacao.id_usuario_destino]")

    _default_fields = [
        "id_usuario",
        "id_familia",
        "nome",
        "cpf",
        "endereco",
        "telefone",
        "email"
    ]

    _hidden_fields = [
        "senha"
    ]

    #movimentacoes = db.relationship('Movimentacao', backref = 'usuario')
    #pagamentos = db.relationship('Movimentacao',backref = 'pagador', lazy = "dynamic", foreign_keys = "id_usuario_origem")
    def __init__(self, nome, cpf, endereco, telefone, email, senha):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.senha = senha

    def centralizar(self):
        for conta in self.contas:
            self.saldo_cc += conta.saldo_cc
            self.saldo_pp += conta.saldo_pp
            self.saldo_total += conta.saldo_pp + conta.saldo_cc

class Familia(BaseModel):
    id_familia = db.Column(db.String(15), primary_key = True)
    nome = db.Column(db.String(30), nullable = False)
    senha = db.Column(db.String(30),nullable = False)
    membros = db.relationship('Usuario', backref = 'familia', lazy = True)
    saldo_cc = 0
    saldo_pp = 0
    saldo_total = 0

    _default_fields = [
        "id_familia",
        "nome",
    ]

    _hidden_fields = [
        "senha"
    ]

    def __init__(self, id, nome, senha):
        self.id_familia = id
        self.nome = nome
        self.senha = senha
    
    def adicionar(self,usuario):
        if usuario in self._membros: return False
        self._membros.append(usuario)
        return True
    
    def centralizar(self):
        for usuario in self.membros:
            #usuario.centralizar()
            self.saldo_cc += usuario.saldo_cc
            self.saldo_pp += usuario.saldo_pp
            self.saldo_total += usuario.saldo_total

    def getCentralizedInfo(self):
        return {
            "saldo_cc": self.saldo_cc,
            "saldo_pp": self.saldo_pp,
            "saldo_total": self.saldo_total
        }

class Conta(BaseModel): #CONSERTAR https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#simple-example
    id_banco = db.Column(db.Integer)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    agencia = db.Column(db.Integer, nullable = False)
    cc = db.Column(db.Integer, nullable = False)
    saldo_cc = db.Column(db.Numeric, default = 0)
    saldo_pp = db.Column(db.Numeric, default = 0)

    __table_args__ = (PrimaryKeyConstraint('id_banco', 'id_usuario'),)

    #pagamentos = db.relationship("Movimentacao", primaryjoin = "and_(Conta.id_banco == Movimentacao.id_banco_origem, Conta.id_usuario == Movimentacao.id_usuario_origem)", backref = "conta_origem", foreign_keys = "[Movimentacao.id_banco_origem, Movimentacao.id_usuario_origem]")
    #recebimentos = db.relationship("Movimentacao", primaryjoin = "and_(Conta.id_banco == Movimentacao.id_banco_destino, Conta.id_usuario == Movimentacao.id_usuario_destino)", backref = "conta_destino", foreign_keys = "[Movimentacao.id_banco_destino, Movimentacao.id_usuario_destino]")
    pagamentos = db.relationship("Movimentacao", backref = "conta_origem", 
        primaryjoin = "and_(Conta.id_banco == Movimentacao.id_banco_origem, Conta.id_usuario == Movimentacao.id_usuario_origem)",
        foreign_keys = "[Movimentacao.id_banco_origem, Movimentacao.id_usuario_origem]")
    recebimentos = db.relationship("Movimentacao", backref = "conta_destino", 
        primaryjoin = "and_(Conta.id_banco == Movimentacao.id_banco_destino, Conta.id_usuario == Movimentacao.id_usuario_destino)",
        foreign_keys = "[Movimentacao.id_banco_destino, Movimentacao.id_usuario_destino]")
    _default_fields = [
        "id_banco",
        "id_usuario",
        "agencia",
        "cc",
        "saldo_cc",
        "saldo_pp"
    ]

    
    #movimentacoes = db.relationship('Movimentacao', backref = 'conta', lazy = True)
    def __init__(self, id_banco, id_usuario, agencia, cc):
        self.id_banco = id_banco
        self.id_usuario = id_usuario
        self.agencia = agencia
        self.cc = cc
        self.saldo_cc = 0
        self.saldo_pp = 0
        self.extrato = []

class Movimentacao(BaseModel):
    id_banco_origem = db.Column(db.Integer)
    id_usuario_origem = db.Column(db.Integer)
    id_banco_destino = db.Column(db.Integer)
    id_usuario_destino = db.Column(db.Integer)
    
    
    #banco_origem = db.relationship("Conta", backref = "origem", foreign_keys = "[Movimentacao.id_banco_origem, Movimentacao.id_usuario.origem]")
    #banco_destino = db.relationship("Conta", backref = "destino", foreign_keys = "[Movimentacao.id_banco_destino, Movimentacao.id_usuario_destino]")
    #usuario_origem = db.relationship("Conta", backref = "usuario_origem", foreign_keys = "[Movimentacao.id_usuario_origem]")
    #usuario_destino = db.relationship("Conta", backref = "usuario_destino", foreign_keys = "[Movimentacao.id_usuario_destino]")
    data_hora = db.Column(db.DateTime)
    valor = db.Column(db.Numeric, nullable = False)
    descricao = db.Column(db.String(100), nullable = True)

    __table_args__ = (
        PrimaryKeyConstraint('id_banco_origem', 'id_banco_destino', 'id_usuario_origem', 'id_usuario_destino', 'data_hora'),
        ForeignKeyConstraint(['id_banco_origem','id_usuario_origem'], ['conta_origem.id_banco', 'conta_origem.id_usuario']),
        ForeignKeyConstraint(['id_banco_destino','id_usuario_destino'], ['conta_destino.id_banco','conta_destino.id_usuario'])
    )

    _default_fields = [
        "id_banco_origem",
        "id_usuario_origem",
        "id_banco_destino",
        "id_usuario_destino",
        "data_hora",
        "valor",
        "descricao"
    ]

    def __init__(self, id_banco_origem, id_banco_destino, id_usuario_origem, id_usuario_destino, data_hora, valor, descricao):
        self.id_banco_origem = id_banco_origem
        self.id_banco_destino = id_banco_destino
        self.id_usuario_origem = id_usuario_origem
        self.id_usuario_destino = id_usuario_destino
        self.data_hora = data_hora
        self.valor = valor
        self.descricao = descricao