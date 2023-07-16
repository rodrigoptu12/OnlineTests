from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import Exame, Question, Item, User, Resposta
from dotenv import load_dotenv
import os
from database.database import db

load_dotenv()

def popular_banco_dados():
    # Popula as entidades User
    user1 = User(name='John Doe', email='john.doe@example.com', registration=12345, password_hash='hashed_password', is_teacher=True)
    user2 = User(name='Jane Smith', email='jane.smith@example.com', registration=67890, password_hash='hashed_password', is_teacher=True)
    user3 = User(name='Alice Johnson', email='alice.johnson@example.com', registration=54321, password_hash='hashed_password', is_teacher=False)

    # Popula as entidades Exame
    exame1 = Exame(titulo='Exame 1', inicio=datetime.now(), professor_id=1)
    exame2 = Exame(titulo='Exame 2', inicio=datetime.now(), professor_id=1)
    exame3 = Exame(titulo='Exame 3', inicio=datetime.now(), professor_id=2)

    # Popula as entidades Question
    question1 = Question(command='Qual é a capital do Brasil?', answer_key='Brasília', question_type='Múltipla escolha', exame_id=1)
    question2 = Question(command='Quem descobriu a América?', answer_key='Cristóvão Colombo', question_type='Verdadeiro ou Falso', exame_id=1)
    question3 = Question(command='Quanto é 2 + 2?', answer_key='4', question_type='Resposta curta', exame_id=1)

    # Popula as entidades Item
    item1 = Item(text='A) Rio de Janeiro', question_id=1)
    item2 = Item(text='B) São Paulo', question_id=1)
    item3 = Item(text='C) Brasília', question_id=1)
    item4 = Item(text='D) Salvador', question_id=1)
    item5 = Item(text='Verdadeiro', question_id=1)
    item6 = Item(text='Falso', question_id=1)

    # Popula as entidades Resposta
    resposta1 = Resposta(aluno_id=1, exame_id=1, respostas={'1': 'C'})
    resposta2 = Resposta(aluno_id=2, exame_id=1, respostas={'1': 'B'})
    resposta3 = Resposta(aluno_id=3, exame_id=1, respostas={'1': '4'})

    # Adiciona as entidades ao banco de dados
    db.session.add_all([user1, user2, user3, exame1, exame2, exame3, question1, question2, question3, item1, item2, item3, item4, item5, item6, resposta1, resposta2, resposta3])
    db.session.commit()
