# 💰 Sistema Financeiro Simplificado

## 📝 Descrição do Sistema
[cite_start]Este projeto consiste em uma aplicação backend desenvolvida para a avaliação de Primeira Menção da disciplina[cite: 1, 3]. [cite_start]O objetivo é oferecer uma ferramenta de controle financeiro pessoal que permite aos usuários gerenciarem suas receitas e despesas de forma organizada e segura[cite: 22]. [cite_start]A aplicação foi construída utilizando **Python + Flask** e integra-se a um banco de dados relacional para persistência de dados[cite: 3, 35].

---

## 🗄️ Estrutura do Banco de Dados
[cite_start]O sistema utiliza uma estrutura de banco de dados relacional com 4 tabelas, garantindo a organização e a integridade das informações através de chaves primárias e estrangeiras[cite: 39, 41]:

* [cite_start]**Usuários (`usuarios`)**: Tabela para cadastro de usuários do sistema[cite: 44].
* [cite_start]**Categorias (`categorias`)**: Tabela auxiliar para classificar os tipos de gastos ou ganhos (ex: Alimentação, Lazer, Salário)[cite: 23, 46].
* [cite_start]**Lançamentos (`lancamentos`)**: Tabela principal que armazena os registros financeiros[cite: 45].
* [cite_start]**Histórico (`historico_transacoes`)**: Tabela de relacionamento ou histórico para auditoria das movimentações[cite: 47].

---

## 🚀 Lista de Rotas
[cite_start]A aplicação implementa um CRUD completo integrado ao banco de dados[cite: 48, 54]:

* [cite_start]**`POST /usuarios`**: Cadastro de novos usuários[cite: 50].
* **`GET /categorias`**: Listagem de categorias cadastradas[cite: 51].
* [cite_start]**`POST /lancamentos`**: Criação de um novo registro financeiro[cite: 50].
* [cite_start]**`GET /lancamentos`**: Consulta de todos os lançamentos[cite: 51].
* **`PUT /lancamentos/<id>`**: Atualização de dados de um lançamento específico[cite: 52].
* [cite_start]**`DELETE /lancamentos/<id>`**: Remoção de um registro do banco de dados[cite: 53].

---

## ⚖️ Regras de Negócio
[cite_start]Para atender aos requisitos do projeto, as seguintes regras foram implementadas[cite: 24]:

1.  [cite_start]**Valor Positivo**: Todo lançamento financeiro deve, obrigatoriamente, possuir um valor maior que zero[cite: 24].
2.  [cite_start]**Associação de Categoria**: É obrigatório que todo lançamento esteja associado a uma categoria existente[cite: 24].
3.  [cite_start]**Consistência Semântica**: Cada lançamento deve ser classificado estritamente como "entrada" ou "saída"[cite: 24].

---

## 🛠️ Instruções para Execução

### 1. Preparar Ambiente Virtual
[cite_start]O projeto utiliza `venv` para isolamento de dependências[cite: 60, 61].
```bash
python -m venv venv
# Ativar no Windows:
venv\Scripts\activate
# Ativar no Linux/Mac:
source venv/bin/activate
