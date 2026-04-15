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

🔗 Rotas Disponíveis

O sistema está organizado em módulos (Blueprints) para separar a lógica de autenticação da lógica de negócios:
1. Autenticação (Blueprint: auth)

    /auth/login: Exibe o formulário de login e processa a autenticação do usuário. (Renderiza: auth/login.html)

    /auth/cadastro: Permite o registro de novos usuários no sistema. (Renderiza: auth/cadastro.html)

    /auth/logout: Encerra a sessão do usuário atual.

2. Gestão Financeira (Blueprint: transacoes)

    / ou /transacoes/: Dashboard principal com o resumo financeiro e a listagem das transações do usuário logado. (Renderiza: transacoes/lista.html)

    /transacoes/cadastrar: Exibe o formulário para adicionar uma nova entrada ou saída. (Renderiza: transacoes/form.html)

    /transacoes/editar/<int:id>: Carrega os dados de uma transação específica para edição. (Renderiza: transacoes/form.html)

    /transacoes/deletar/<int:id>: Rota interna para excluir uma transação e redirecionar para a listagem.

3. Metas (Integrada em transacoes ou módulo próprio)

    /metas/: Visualização e acompanhamento das metas financeiras definidas (com base no seu arquivo models.py).

📦 Como Executar o Projeto

    Certifique-se de ter o MySQL rodando e crie o banco db_financeiro.

    Importe o arquivo banco.sql disponível na raiz.

    Instale as dependências: pip install -r requirements.txt.

    Configure as variáveis de ambiente no arquivo .env (ou config.py).

    Execute o comando: flask run ou python app.py
