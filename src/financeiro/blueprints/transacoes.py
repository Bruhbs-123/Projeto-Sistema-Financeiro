from flask import Blueprint, render_template, request, redirect, url_for, flash
from src.financeiro.models import Transacao
from src.financeiro.extensions import db
from sqlalchemy import func, extract
from datetime import datetime, date

bp = Blueprint('transacoes', __name__)

@bp.route('/')
def lista():
    # 1. Filtros de Data
    mes_selecionado = request.args.get('mes', datetime.now().month, type=int)
    ano_selecionado = request.args.get('ano', datetime.now().year, type=int)

    # 2. Cálculo do Saldo Acumulado (Histórico total até o mês filtrado)
    if mes_selecionado == 12:
        limite_data = date(ano_selecionado + 1, 1, 1)
    else:
        limite_data = date(ano_selecionado, mes_selecionado + 1, 1)

    historico = Transacao.query.filter(Transacao.data < limite_data).all()
    saldo_total = sum(float(i.valor) if i.tipo == 'receita' else -float(i.valor) for i in historico)

    # 3. Transações do Mês Selecionado (Tabela)
    itens_do_mes = Transacao.query.filter(
        extract('month', Transacao.data) == mes_selecionado,
        extract('year', Transacao.data) == ano_selecionado
    ).order_by(Transacao.data.desc()).all()

    # 4. Resumo por Categoria (Gráfico e Cards)
    resumo_query = db.session.query(
        Transacao.categoria, 
        func.sum(Transacao.valor)
    ).filter(
        Transacao.tipo == 'despesa',
        extract('month', Transacao.data) == mes_selecionado,
        extract('year', Transacao.data) == ano_selecionado
    ).group_by(Transacao.categoria).all()

    # 5. Preparação dos dados do Gráfico (Garante que não venha vazio)
    labels_grafico = [str(item[0]) if item[0] else "Geral" for item in resumo_query]
    valores_grafico = [float(item[1]) for item in resumo_query]

    # ÚNICO RETURN - Envia tudo para o HTML
    return render_template(
        'transacoes/lista.html', 
        transacoes=itens_do_mes, 
        saldo=saldo_total, 
        resumo=resumo_query, 
        mes_atual=mes_selecionado,
        ano_atual=ano_selecionado,
        labels_json=labels_grafico,
        valores_json=valores_grafico
    )

@bp.route('/nova', methods=['GET', 'POST'])
def nova():
    if request.method == 'POST':
        try:
            desc = request.form.get('descricao')
            val_input = request.form.get('valor')
            tip = request.form.get('tipo')
            categoria = request.form.get('categoria')

            val = float(val_input.replace(',', '.'))
            if val <= 0:
                flash("O valor deve ser maior que zero!", "warning")
                return redirect(url_for('transacoes.nova'))

            t = Transacao(descricao=desc, valor=val, tipo=tip, categoria=categoria, user_id=1)
            db.session.add(t)
            db.session.commit()
            flash("Transação salva com sucesso!", "success")
            return redirect(url_for('transacoes.lista'))
        except Exception:
            flash("Erro ao processar o valor. Use apenas números.", "danger")
            return redirect(url_for('transacoes.nova'))
    return render_template('transacoes/form.html')

@bp.route('/deletar/<int:id>', methods=['POST'])
def deletar(id):
    t = Transacao.query.get_or_404(id)
    db.session.delete(t)
    db.session.commit()
    flash("Removido!", "success")
    return redirect(url_for('transacoes.lista'))