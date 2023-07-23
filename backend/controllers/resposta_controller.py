from flask import request
from flask_restful import Resource
from models.resposta import Resposta
from database.database import db
from flask import Blueprint

resposta_bp = Blueprint('resposta', __name__)


class RespostaController(Resource):

    @resposta_bp.route('/resposta', methods=['POST'])
    def post():
        data = request.get_json()
        id_aluno = data.get('id_aluno')
        id_exame = data.get('id_exame')
        respostas = data.get('respostas')

        resposta = Resposta(aluno_id=id_aluno,
                            exame_id=id_exame,
                            respostas=respostas)

        db.session.add(resposta)
        db.session.commit()

        return {'message': 'Resposta criada com sucesso'}, 201
    

    @resposta_bp.route('/resposta/<int:id_exame>', methods=['GET'])
    def get(id_exame):
        respostas = Resposta.query.filter_by(exame_id=id_exame).all()

        respostas_json = []
        for resposta in respostas:
            resposta_data = {
                'id': resposta.id,
                'id_aluno': resposta.aluno_id,
                'id_exame': resposta.exame_id,
                'respostas': resposta.respostas,
                'date': resposta.date.strftime("%Y-%m-%d %H:%M:%S")
            }
            respostas_json.append(resposta_data)

        return {'respostas': respostas_json}
    
    @resposta_bp.route('/resposta/<int:id_exame>/<int:id_aluno>', methods=['GET'])
    def verify_answer(id_exame, id_aluno):
        resposta = Resposta.query.filter_by(exame_id=id_exame, aluno_id=id_aluno).first()

        if resposta is not None:
            return {'resposta': True}
        else:
            return {'resposta': False}
