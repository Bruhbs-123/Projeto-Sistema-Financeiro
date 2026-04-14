from flask import Blueprint, render_template, request, redirect, url_for, flash
from src.financeiro.models import Transacao, Categoria
from src.financeiro.extensions import db
from sqlalchemy import func, extract
from datetime import datetime, date
from flask import session

bp = Blueprint('transacoes', __name__)

@bp.route('/')
def lista():
    mes_selecionado = request.args.get('mes', datetime.now().month, type=int)
    ano_selecionado = request.args.get('ano', datetime.now().year, type=int)

    if mes_selecionado == 12:
        limite_data = date(ano_selecionado + 1, 1, 1)
    else:
        limite_data = date(ano_selecionado, mes_selecionado + 1, 1)

    historico = Transacao.query.filter(Transacao.data < limite_data).all()
    saldo_total = sum(float(i.valor) if i.tipo == 'receita' else -float(i.valor) for i in historico)

    itens_do_mes = Transacao.query.filter(
        extract('month', Transacao.data) == mes_selecionado,
        extract('year', Transacao.data) == ano_selecionado
    ).order_by(Transacao.data.desc()).all()

    resumo_query = db.session.query(
        Categoria.nome, 
        func.sum(Transacao.valor)
    ).join(Categoria).filter(
        Transacao.tipo == 'despesa',
        extract('month', Transacao.data) == mes_selecionado,
        extract('year', Transacao.data) == ano_selecionado
    ).group_by(Categoria.nome).all()

    cores_map = {
        'Alimentação': '#8A05BE', 'Lazer': '#BC58FF', 
        'Moradia': '#4B0082', 'Saúde': '#E0AAFF', 
        'Transporte': '#3D0066', 'Outros': '#9D4EDD'
    }

    labels_grafico = [str(item[0]) for item in resumo_query]
    valores_grafico = [float(item[1]) for item in resumo_query]
    cores_lista = [cores_map.get(label, '#CFCFC4') for label in labels_grafico]

    return render_template(
        'transacoes/lista.html', 
        transacoes=itens_do_mes, 
        saldo=saldo_total, 
        resumo=resumo_query, 
        mes_atual=mes_selecionado,
        ano_atual=ano_selecionado,
        labels_json=labels_grafico,
        valores_json=valores_grafico,
        cores_json=cores_lista
    )

@bp.route('/nova', methods=['GET', 'POST'])
def nova():
    categorias = Categoria.query.all()
    if request.method == 'POST':
         nova_t = Transacao(
            descricao=request.form.get('descricao'),
            valor=request.form.get('valor'),
            tipo=request.form.get('tipo'),
            categoria_id=request.form.get('categoria_id'),
            data=datetime.now(),
            user_id=session.get('user_id')
       )
        
        
         db.session.add(nova_t)
         db.session.commit()
         return redirect(url_for('transacoes.lista'))
    return render_template('transacoes/form.html', categorias=categorias)

@bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    t = Transacao.query.get_or_404(id)
    categorias = Categoria.query.all()
    if request.method == 'POST':
        t.descricao = request.form.get('descricao')
        t.valor = request.form.get('valor')
        t.tipo = request.form.get('tipo')
        t.categoria_id = request.form.get('categoria_id')
        db.session.commit()
        return redirect(url_for('transacoes.lista'))
    return render_template('transacoes/form.html', transacao=t, categorias=categorias)

@bp.route('/deletar/<int:id>', methods=['POST'])
def deletar(id):
    t = Transacao.query.get_or_404(id)
    db.session.delete(t)
    db.session.commit()
    return redirect(url_for('transacoes.lista'))

