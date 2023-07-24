from flask import request, jsonify
from flask_restful import Resource
from models.resposta import Resposta
from models.exame import Exame
from models.question import Question
from datetime import datetime
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
    
    @resposta_bp.route('/resposta/<int:exame_id>/<int:aluno_id>', methods=['GET'])
    def verify_answer(exame_id, aluno_id):
        resposta = Resposta.query.filter_by(exame_id=exame_id, aluno_id=aluno_id).first()

        if resposta is not None:
            return {'resposta': True}
        else:
            return {'resposta': False}
        
    @resposta_bp.route('/resposta/nota/<int:exame_id>/<int:aluno_id>', methods=['GET'])
    def calcular_nota(exame_id, aluno_id):
        exame = Exame.query.get(exame_id)
        
        if not exame:
            return jsonify({"error": "Exame não encontrado"}), 404

        if exame.fim and exame.fim > datetime.utcnow():
            return jsonify({"error": "O exame ainda não foi finalizado"}), 400

        questoes = Question.query.filter_by(exame_id=exame_id).all()

        respostas = Resposta.query.filter_by(exame_id=exame_id, aluno_id=aluno_id).first()

        if not respostas:
            return jsonify({"error": "Respostas do aluno não encontradas"}), 404

        respostas_aluno = respostas.respostas

        nota_total = 0
        for questao in questoes:
            questao_id = questao.id
            resposta_aluno = next((resposta['resposta'] for resposta in respostas_aluno if resposta['id'] == str(questao_id)), None)
            if resposta_aluno is not None:
                resposta_correta = questao.answer_key
                if resposta_aluno == resposta_correta:
                    nota_total += questao.value

        return jsonify({"nota": nota_total})

