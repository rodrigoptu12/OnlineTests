# Requisitos para o Sistema de Lista de Presença em Aulas

## Visão Geral

O objetivo deste sistema é facilitar o processo de registro de presença dos alunos em aulas, sem que o professor precise fazê-lo manualmente. A solução será um SaaS (Software as a Service), desenvolvido com o framework Flask em Python.

## Requisitos Funcionais

- O professor deve ser capaz de gerar um QR Code/Código que será utilizado pelos alunos para confirmar sua presença na aula.
- O aluno deve escanear o QR Code/Código gerado pelo professor, utilizando a câmera do seu dispositivo móvel ou colocar o código, para confirmar sua presença.
- O sistema deve verificar a localização do aluno para garantir que ele está presente na aula.
- O sistema deve registrar a presença do aluno na aula em tempo real.
- O professor deve ter acesso a uma lista de presença atualizada em tempo real.

## Requisitos Não Funcionais

- O sistema deve ser desenvolvido com o framework Flask em Python.
- O sistema deve ser hospedado em um servidor web confiável e seguro.
- O sistema deve ser fácil de usar e intuitivo para professores e alunos.
- O sistema deve ser escalável e capaz de lidar com grandes quantidades de alunos.

## Funcionalidades Adicionais

- O sistema pode enviar uma notificação para o professor quando um aluno chegar atrasado ou sair da aula antes do término.
- O sistema pode gerar relatórios de presença para cada aula ou para um período específico.

## Conclusão

Este documento descreve os requisitos para um Sistema de Lista de Presença em Aulas baseado na localização do aluno e utilizando um QR Code gerado pelo professor. O sistema deve ser fácil de usar, seguro e capaz de lidar com grandes quantidades de alunos. Esperamos que este sistema facilite o processo de registro de presença dos alunos nas aulas e melhore a eficiência do processo para professores e alunos.

## Instruções para Executar o Projeto
- Instale o Python 3.x em seu computador, caso ainda não tenha instalado.
- Clone o repositório do projeto em sua máquina: git clone https://github.com/seu-usuario/projeto-flask-python.git
- Crie e ative um ambiente virtual para o projeto: python -m venv venv e source venv/bin/activate (Linux/Mac) ou venv\Scripts\activate (Windows)
- Instale as dependências do projeto: pip install -r requirements.txt
- Execute o projeto: flask run
- Acesse a aplicação em seu navegador através do endereço http://localhost:5000