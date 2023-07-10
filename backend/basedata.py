from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import Exame, Question, Item, User
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy(app)


# Função para inserir dados no banco de dados
def populate_database():
    user1 = User(
        name='Professor',
        email='professor0@example.com',
        registration=10011,
        password_hash='password1',
        is_teacher=True
    )
    user2 = User(
        name='Professor 2',
        email='professor2@example.com',
        registration=10020,
        password_hash='password2',
        is_teacher=True
    )
    user3 = User(
        name='Aluno',
        email='fulano0@example.com',
        registration=10030,
        password_hash='password3',
        is_teacher=False
    )
    user4 = User(
        name='Aluno 2',
        email='fulano20@example.com',
        registration=10040,
        password_hash='password4',
        is_teacher=False
    )
    # Criação de objetos Exame
    exame1 = Exame(
        titulo='Exame 1',
        inicio=datetime(2023, 7, 10),
        fim=datetime(2023, 1, 15),
        estado='aberto',
        professor_id=1
    )
    exame2 = Exame(
        titulo='Exame 2',
        inicio=datetime(2024, 2, 1),
        fim=datetime(2024, 2, 2),
        estado='agendado',
        professor_id=2
    )
    exame3 = Exame(
        titulo='Exame 3',
        inicio=datetime(2022, 1, 1),
        fim=datetime(2022, 1, 2),
        estado='fechado',
        professor_id=1
    )
    exame4 = Exame(
        titulo='Exame 4',
        inicio=datetime(2021, 1, 1),
        fim=datetime(2021, 1, 2),
        estado='fechado',
        professor_id=2
    )
    # Criação de objetos Question
    question1 = Question(
        command='Pergunta 1',
        answer_key='Resposta 1',
        question_type='Tipo 1',
        exame_id=1
    )
    question2 = Question(
        command='Pergunta 2',
        answer_key='Resposta 2',
        question_type='Tipo 2',
        exame_id=2
    )

    # Criação de objetos Item
    item1 = Item(
        text='Item 1',
        question_id=1
    )
    item2 = Item(
        text='Item 2',
        question_id=2
    )

    # Persistir objetos no banco de dados
    db.session.add_all([user1, user2, user3, user4, exame1, exame2, exame3,
                        exame4, question1, question2, item1, item2])
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        populate_database()
    app.run(debug=True)
