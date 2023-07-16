# Realização de testes online

Este projeto foi desenvolvido como trabalho final da disciplina de Engenharia de Software

## Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas em seu ambiente de desenvolvimento:

- Node.js (versão 18 ou superior)
- Python (versão 3.x)

## Instalação

1. Clone este repositório em sua máquina local:

### Backend

1.  Acesse o diretório do projeto pelo terminal:

        cd backend

2.  Crie um ambiente virtual para o seu projeto.  

        python -m venv env

3.  Ative o ambiente virtual.
   
   3.1.  No Windows:

        env\Scripts\activate

   3.2.  No macOS/Linux:

        source env/bin/activate
  
4.  Instale as dependências do projeto:

        pip install -r requirements.txt --no-dependencies

5.  Configure o banco de dados

Antes de executar o sistema, é necessário configurar as informações de conexão com o banco de dados. Crie o arquivo `.env` dentro da pasta backend, e preencha as informações necessárias, como nome de usuário, senha e nome do banco de dados.

        SQLALCHEMY_DATABASE_URI=postgresql://user:password@host/databaseName

Certifique-se de ter um servidor de banco de dados postgreSQL (pode criá-lo pelo pgAdmin 4, disponível em postgresql.org) em execução e que o banco de dados especificado esteja criado.

7. Execute o comando para iniciar a aplicação:

        flask run




### Frontend

1.  Abra outro terminal

2.  Acesse o diretório do projeto:

        cd frontend/src

3.  Instale as dependências do projeto:

        yarn install

4. Execute o comando para iniciar a aplicação:
    
        yarn dev

5. Abra, no navegador, http://127.0.0.1:5173/


### Observações:

Ao criar a conta, crie uma senha de no mínimo 8 caracteres e matrícula de 9 dígitos. Caso ao clicar em criar conta, não seja redirecionado para outra tela, mude manualmente para a de login. O mesmo acontece quando se cria uma questão, e depois no exame, ao clicar em criar exame, não for redirecionado para a tela de exames, mude manualmente para a tela de exames.
   
