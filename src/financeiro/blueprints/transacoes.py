from flask import Blueprint, render_template, request, redirect, url_for, flash
from src.financeiro.models import Transacao
from src.financeiro.extensions import db

bp = Blueprint('transacoes', __name__)

@bp.route('/')
def lista():
    itens = Transacao.query.all()
    # Regra de Negócio: Cálculo de Saldo
    saldo = sum(float(i.valor) if i.tipo == 'receita' else -float(i.valor) for i in itens)
    return render_template('transacoes/lista.html', transacoes=itens, saldo=saldo)

@bp.route('/nova', methods=['GET', 'POST'])
def nova():
    if request.method == 'POST':
        desc = request.form['descricao']
        val = float(request.form['valor'])
        tip = request.form['tipo']

        # Regra de Negócio: Impedir valor negativo
        if val <= 0:
            flash("O valor deve ser positivo!")
            return redirect(url_for('transacoes.nova'))

        # CORREÇÃO AQUI: Adicionado user_id=1 para satisfazer a chave estrangeira
        t = Transacao(descricao=desc, valor=val, tipo=tip, user_id=1)
        
        db.session.add(t)
        db.session.commit()
        return redirect(url_for('transacoes.lista'))
        
    return render_template('transacoes/form.html')