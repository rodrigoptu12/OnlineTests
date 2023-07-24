from datetime import datetime, timedelta
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import Exame, Question, Item, User, Resposta
from dotenv import load_dotenv
import os
from database.database import db
from werkzeug.security import generate_password_hash

load_dotenv()

def popular_banco_dados():
    data_hora_atual = datetime.now()
    data_hora_fim = data_hora_atual + timedelta(hours=2)

    data_hora_inicio_encerrado = data_hora_atual - timedelta(days=1) - timedelta(hours=2)
    data_hora_fim_encerrado = data_hora_atual - timedelta(days=1)

    data_hora_inicio_agendado = data_hora_atual + timedelta(days=1)
    data_hora_fim_agendado = data_hora_atual + timedelta(days=1) + timedelta(hours=2)

    # Popula as entidades User
    user1 = User(name='pedro', email='pedro@unb.br', registration=12345, password_hash=generate_password_hash('asdfg'), is_teacher=True)
    user2 = User(name='Jane Smith', email='jane.smith@example.com', registration=67890, password_hash=generate_password_hash('12345678'), is_teacher=True)
    user3 = User(name='ester', email='ester@unb.br', registration=54321, password_hash=generate_password_hash('asdfg'), is_teacher=False)

    # Popula as entidades Exame
    exame1 = Exame(titulo='Exame 1', inicio=data_hora_inicio_encerrado, fim=data_hora_fim_encerrado,  professor_id=1)
    exame2 = Exame(titulo='Exame 2', inicio=data_hora_inicio_encerrado, fim=data_hora_fim_encerrado,  professor_id=1)

    exame3 = Exame(titulo='Exame 3', inicio=data_hora_atual, fim=data_hora_fim, professor_id=2)
    exame4 = Exame(titulo='Exame 4', inicio=data_hora_atual, fim=data_hora_fim, professor_id=2)

    exame5 = Exame(titulo='Exame 5', inicio=data_hora_inicio_agendado, fim=data_hora_fim_agendado, professor_id=1)
    exame6 = Exame(titulo='Exame 6', inicio=data_hora_inicio_agendado, fim=data_hora_fim_agendado, professor_id=2)

    # Popula as entidades Question
    question1 = Question(command='Qual é a capital do Brasil?', answer_key='Brasília', question_type='Múltipla escolha', exame_id=1, value=10)
    question2 = Question(command='Quem descobriu a América foi Cristóvão Colombo?', answer_key='Verdadeiro', question_type='Verdadeiro ou Falso', exame_id=2, value=1)
    question3 = Question(command='Quanto é 2 + 2?', answer_key='4', question_type='Resposta curta', exame_id=3, value=3)

    question4 = Question(command='Qual é o maior planeta do sistema solar?', answer_key='Júpiter', question_type='Múltipla escolha', exame_id=4, value=2)
    question5 = Question(command='Quem escreveu a obra "Dom Quixote"?', answer_key='Miguel de Cervantes', question_type='Resposta curta', exame_id=5, value=3)

    question6 = Question(command='Qual é a capital do Brasil?', answer_key='Brasília', question_type='Múltipla escolha', exame_id=6, value=10)
    question7 = Question(command='Quem descobriu a América foi Cristóvão Colombo?', answer_key='Verdadeiro', question_type='Verdadeiro ou Falso', exame_id=4, value=1)

    question8 = Question(command='Qual é a capital do Brasil?', answer_key='Brasília', question_type='Múltipla escolha', value=10)
    question9 = Question(command='Quem descobriu a América foi Cristóvão Colombo?', answer_key='Verdadeiro', question_type='Verdadeiro ou Falso', value=1)

    question10 = Question(command='Qual é o maior planeta do sistema solar?', answer_key='Júpiter', question_type='Múltipla escolha', value=2)
    question11 = Question(command='Quem escreveu a obra "Dom Quixote"?', answer_key='Miguel de Cervantes', question_type='Resposta curta', value=3)

    # Popula as entidades Item
    item1 = Item(text='Rio de Janeiro', question_id=1)
    item2 = Item(text='São Paulo', question_id=1)
    item3 = Item(text='Brasília', question_id=1)
    item4 = Item(text='Salvador', question_id=1)
    item5 = Item(text='Verdadeiro', question_id=7)
    item6 = Item(text='Falso', question_id=7)

    item7 = Item(text='Saturno', question_id=4)
    item8 = Item(text='Marte', question_id=4)
    item9 = Item(text='Júpiter', question_id=4)
    item10 = Item(text='Vênus', question_id=4)
    item11 = Item(text='Miguel de Cervantes', question_id=5)
    item12 = Item(text='William Shakespeare', question_id=5)
    item13 = Item(text='Charles Dickens', question_id=5)

    # Popula as entidades Resposta
    resposta1 = Resposta(aluno_id=3, exame_id=1, respostas=[{'id': '1', 'resposta': 'Brasília'}])
    resposta2 = Resposta(aluno_id=3, exame_id=3, respostas=[{'id': '3', 'resposta': '2'}])

    # Adiciona as entidades ao banco de dados
    db.session.add_all([user1, user2, user3, exame1, exame2, exame3, exame4, exame5, exame6, question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, resposta1, resposta2])
    db.session.commit()
