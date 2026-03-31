from src.financeiro.extensions import db
from datetime import datetime

class User(db.Model):  # Verifique se o nome é EXATAMENTE 'User'
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    transacoes = db.relationship('Transacao', backref='usuario', lazy=True)

class Transacao(db.Model): # Verifique se esta classe também existe
    __tablename__ = 'transacoes'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200), nullable=False)
    valor = db.Column(db.Numeric(10, 2), nullable=False)
    tipo = db.Column(db.String(10), nullable=False)
    data = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)