from src.financeiro.extensions import db
from datetime import datetime

# 1. Tabela de Usuários (Obrigatória) [cite: 44]
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    # Relacionamento: Um usuário tem muitas transações
    transacoes = db.relationship('Transacao', backref='autor', lazy=True)
    # Relacionamento: Um usuário tem muitas metas
    metas = db.relationship('Meta', backref='usuario', lazy=True)

# 2. Tabela Auxiliar: Categorias (Obrigatória) [cite: 46]
class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False, unique=True)
    transacoes = db.relationship('Transacao', backref='categoria_rel', lazy=True)

# 3. Tabela Principal: Transações (Lançamentos) [cite: 45]
class Transacao(db.Model):
    __tablename__ = 'transacoes'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(255), nullable=False)
    valor = db.Column(db.Numeric(10, 2), nullable=False) # Regra: Valor deve ser positivo 
    tipo = db.Column(db.String(10), nullable=False) # 'entrada' ou 'saida' 
    data = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Chaves Estrangeiras (Relacionamentos) 
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)

# 4. Tabela de Relacionamento/Histórico: Metas Financeiras (Obrigatória) [cite: 47]
class Meta(db.Model):
    __tablename__ = 'metas'
    id = db.Column(db.Integer, primary_key=True)
    objetivo = db.Column(db.String(100), nullable=False)
    valor_alvo = db.Column(db.Numeric(10, 2), nullable=False)
    mes_referencia = db.Column(db.Integer, nullable=False) # 1 a 12
    ano_referencia = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)