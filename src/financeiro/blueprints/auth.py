from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from src.financeiro.models import Usuario
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

        if Usuario.query.filter_by(email=email).first():
            flash("E-mail já cadastrado!", "warning")
            return redirect(url_for('auth.cadastro'))

        novo_usuario = Usuario(nome=nome, email=email, senha=senha)
        db.session.add(novo_usuario)
        db.session.commit()

        flash("Usuário criado com sucesso! Faça login.", "success")
        return redirect(url_for('auth.login'))

    return render_template('auth/cadastro.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        usuario = Usuario.query.filter_by(email=email, senha=senha).first()

        if not usuario:
            flash("E-mail ou senha incorretos!", "danger")
            return redirect(url_for('auth.login'))

        session['user_id'] = usuario.id
        session['user_nome'] = usuario.nome
        flash(f"Bem-vinda, {usuario.nome}! 👋", "success")
        return redirect(url_for('transacoes.lista'))

    return render_template('auth/login.html')


@bp.route('/logout')
def logout():
    session.clear()
    flash("Você saiu da conta.", "info")
    return redirect(url_for('auth.login'))