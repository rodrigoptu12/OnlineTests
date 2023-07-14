# Realização de testes online

Este projeto foi desenvolvido como trabalho final da disciplina de Engenharia de Software

## Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas em seu ambiente de desenvolvimento:

- Node.js (versão 18 ou superior)
- Python (versão 3.x)

## Instalação

1. Clone este repositório em sua máquina local:

### Backend

1.  Acesse o diretório do projeto:

        cd backend

2.  Instale as dependências do projeto:

        pip install -r requirements.txt

3. Execute o comando para iniciar a aplicação:

        flask run

4. Logo apos execute o comando para popular o banco de dados:
    
        python3 basedata.py

5. Execute o comando para iniciar a aplicação:

        flask run

## Configuração backend

Antes de executar o sistema, é necessário configurar as informações de conexão com o banco de dados. No arquivo `.env`, localize a seção de configuração do banco de dados e preencha as informações necessárias, como nome de usuário, senha e nome do banco de dados.

        SQLALCHEMY_DATABASE_URI=postgresql://user:password@host/databaseName

Certifique-se de ter um servidor de banco de dados postgreSQL em execução e que o banco de dados especificado esteja criado.

### Frontend

2.  Acesse o diretório do projeto:

        cd frontend/src

3.  Instale as dependências do projeto:

        yarn install

4. Execute o comando para iniciar a aplicação:
    
        yarn dev