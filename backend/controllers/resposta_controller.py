from flask import request
from flask_restful import Resource
from models.resposta import Resposta
from database.database import db


class RespostaController(Resource):

    def post(self):
        data = request.get_json()
        id_aluno = data.get('id_aluno')
        id_exame = data.get('id_exame')
        respostas = data.get('respostas')

        resposta = Resposta(id_aluno=id_aluno,
                            id_exame=id_exame,
                            respostas=respostas)

        db.session.add(resposta)
        db.session.commit()

        return {'message': 'Resposta criada com sucesso'}, 201

    def get(self, id_exame):
        respostas = Resposta.query.filter_by(id_exame=id_exame).all()

        respostas_json = []
        for resposta in respostas:
            resposta_data = {
                'id': resposta.id,
                'id_aluno': resposta.id_aluno,
                'id_exame': resposta.id_exame,
                'respostas': resposta.respostas,
                'date': resposta.date.strftime("%Y-%m-%d %H:%M:%S")
            }
            respostas_json.append(resposta_data)

        return {'respostas': respostas_json}
