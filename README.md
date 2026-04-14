# 💰 Sistema Financeiro Simplificado

## 📝 Descrição do Sistema
Este projeto consiste em uma aplicação backend desenvolvida para a avaliação de Primeira Menção da disciplina. O objetivo é oferecer uma ferramenta de controle financeiro pessoal que permite aos usuários gerenciarem suas receitas e despesas de forma organizada e segura. A aplicação foi construída utilizando **Python + Flask** e integra-se a um banco de dados relacional para persistência de dados.

---

## 🗄️ Estrutura do Banco de Dados
O sistema utiliza uma estrutura de banco de dados relacional com 4 tabelas, garantindo a organização e a integridade das informações através de chaves primárias e estrangeiras:

* **Usuários (`usuarios`)**: Tabela para cadastro de usuários do sistema.
* **Categorias (`categorias`)**: Tabela auxiliar para classificar os tipos de gastos ou ganhos (ex: Alimentação, Lazer, Salário).
* **Lançamentos (`lancamentos`)**: Tabela principal que armazena os registros financeiros.
* **Histórico (`historico_transacoes`)**: Tabela de relacionamento ou histórico para auditoria das movimentações.

---

## 🚀 Lista de Rotas
A aplicação implementa um CRUD completo integrado ao banco de dados:

* **`POST /usuarios`**: Cadastro de novos usuários.
* **`GET /categorias`**: Listagem de categorias cadastradas.
* **`POST /lancamentos`**: Criação de um novo registro financeiro.
* **`GET /lancamentos`**: Consulta de todos os lançamentos.
* **`PUT /lancamentos/<id>`**: Atualização de dados de um lançamento específico.
* **`DELETE /lancamentos/<id>`**: Remoção de um registro do banco de dados.

---

## ⚖️ Regras de Negócio
Para atender aos requisitos do projeto, as seguintes regras foram implementadas:

1.  **Valor Positivo**: Todo lançamento financeiro deve, obrigatoriamente, possuir um valor maior que zero.
2.  **Associação de Categoria**: É obrigatório que todo lançamento esteja associado a uma categoria existente.
3.  **Consistência Semântica**: Cada lançamento deve ser classificado estritamente como "entrada" ou "saída".

---

## 🛠️ Instruções para Execução

### 1. Preparar Ambiente Virtual
O projeto utiliza `venv` para isolamento de dependências.
```bash
python -m venv venv
# Ativar no Windows:
venv\Scripts\activate
# Ativar no Linux/Mac:
source venv/bin/activate
venv\Scripts\activate
# Ativar no Linux/Mac:
source venv/bin/activate
