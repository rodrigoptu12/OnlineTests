from flask import request
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
from models.question import Question
from models import db


class QuestionController(Resource):

    def post(self):
        # obtem os dados enviados com a solicitação
        data = request.get_json()
        # cria uma nova questão com os dados recebidos
        new_question = Question(command=data['command'],
                                answer_key=data['answer_key'],
                                question_type=data['question_type'])

        # adiciona a nova questão na sessão do banco de dados
        db.session.add(new_question)

        # realiza commit na sessão para salvar a questão
        db.session.commit()

        return {'message': 'Question created successfully.'}, 201
