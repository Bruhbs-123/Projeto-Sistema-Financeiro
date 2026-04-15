💰 Sistema de Gestão Financeira Pessoal
👥 Equipe e Identificação

    Integrante 1: Bruna Bonifácio Soares Santos - RA: 22509111

    Integrante 2: Rafael Ramos - RA: 22504054

    Integrante 3: Renata Teixeira de Jesus - RA: 

📝 Descrição do Projeto

Este é um sistema web desenvolvido em Python com Flask e MySQL para auxiliar no controle financeiro pessoal. A aplicação permite que o usuário gerencie suas receitas e despesas, visualize o saldo atualizado e acompanhe a distribuição de seus gastos por categorias através de um dashboard interativo.
🚀 Funcionalidades Principais

    Autenticação de Usuários: Cadastro e Login com sessões seguras.

    Dashboard Dinâmico: Gráficos e indicadores de saldo total, entradas e saídas.

    Gestão de Transações: Cadastro, listagem, edição e exclusão de movimentações.

    Gestão de Metas: Planejamento de objetivos financeiros mensais.

    Filtro por Período: Visualização de dados específica por mês e ano.

🛠️ Tecnologias Utilizadas

    Backend: Python 3.x, Flask.

    Banco de Dados: MySQL.

    Frontend: HTML5, CSS3 (Bootstrap 5), JavaScript (Chart.js).

    ORM/Migrações: SQLAlchemy e Flask-Migrate (Alembic).

📊 Estrutura do Banco de Dados (4 Tabelas)

O banco de dados, nomeado como db_financeiro, possui a seguinte estrutura de tabelas:

    usuarios: Armazena nome, e-mail e hash da senha para autenticação.

    categorias: Listagem de categorias (Alimentação, Lazer, Moradia, etc.).

    transacoes: Registro de valores, descrições, tipos (entrada/saída) e datas, vinculados ao usuário e categoria.

    metas: Planejamento de valores alvo por mês/ano para controle de objetivos.

💡 Regras de Negócio Implementadas

Para a demonstração do sistema, destacamos as seguintes regras:

    Isolamento de Dados por Usuário: Cada usuário possui acesso estritamente restrito aos seus próprios dados. O sistema filtra todas as consultas ao banco utilizando o ID da sessão ativa, garantindo privacidade e segurança.

    Filtro de Competência Mensal: O dashboard utiliza funções de extração de data do MySQL para processar e somar transações apenas do mês e ano selecionados. Isso evita a mistura de saldos e fornece uma análise financeira precisa por período.

🔗 Rotas do Sistema

A aplicação está organizada em Blueprints para melhor manutenção:

Módulo de Autenticação (auth):

    /auth/login - Tela de acesso.

    /auth/cadastro - Criação de nova conta.

    /auth/logout - Finalização da sessão.

Módulo Financeiro (transacoes):

    / ou /transacoes/ - Dashboard principal e lista de lançamentos.

    /transacoes/cadastrar - Cadastro de novas receitas/despesas.

    /transacoes/editar/<id> - Edição de registros existentes.

    /transacoes/deletar/<id> - Remoção de registros.

📦 Como Executar o Projeto

    Certifique-se de ter o MySQL rodando e crie o banco db_financeiro.

    Importe o arquivo banco.sql disponível na raiz.

    Instale as dependências: pip install -r requirements.txt.

    Configure as variáveis de ambiente no arquivo .env (ou config.py).

    Execute o comando: flask run ou python app.py
