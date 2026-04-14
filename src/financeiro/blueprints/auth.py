from flask import Blueprint, render_template, request, redirect, url_for, flash
from src.financeiro.models import Usuario # Verifique se o nome no models.py é 'User' ou 'Usuario'
from src.financeiro.extensions import db

bp = Blueprint('auth', __name__)

@bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        if not nome or not email or not senha:
            flash("Preencha todos os campos!", "danger")
            return redirect(url_for('auth.cadastro'))

        # Verifica se já existe
        if Usuario.query.filter_by(email=email).first():
            flash("E-mail já cadastrado!", "warning")
            return redirect(url_for('auth.cadastro'))

        novo_usuario = Usuario(nome=nome, email=email, senha=senha)
        db.session.add(novo_usuario)
        db.session.commit()

        flash("Usuário criado com sucesso!", "success")
        return redirect(url_for('transacoes.lista')) # Leva para a lista após cadastrar

    return render_template('auth/cadastro.html')