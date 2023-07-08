from flask import request
from models import Exame, Question, db
from flask_restful import Resource


class ExameController(Resource):

    def get(self, exame_id=None):
        if exame_id:
            exame = Exame.query.get(exame_id)
            if exame:
                questoes = exame.questoes
                questoes_json = []
                for questao in questoes:
                    questao_data = {
                        'id':
                        questao.id,
                        'titulo':
                        questao.command,
                        'items': [{
                            'id': i.id,
                            'text': i.text
                        } for i in questao.items],
                        'answer_key':
                        questao.answer_key,
                        # Aqui você pode adicionar outros
                        # campos da questão, se necessário
                    }
                    questoes_json.append(questao_data)
                return questoes_json, 200
            else:
                return {'message': 'Exame não encontrado'}, 404
        else:
            exames = Exame.query.all()
            exames_json = []
            for exame in exames:
                exame_data = {
                    'id': exame.id,
                    'titulo': exame.titulo,
                    # Aqui você pode adicionar outros
                    # campos do exame, se necessário
                }
                exames_json.append(exame_data)
            return exames_json, 200

    def post(self):
        data = request.get_json()

        titulo = data.get('titulo')
        questoes_ids = data.get('questoes')

        if titulo and questoes_ids:
            exame = Exame(titulo=titulo)

            # Buscar as questões existentes pelo ID no banco de dados
            questoes = Question.query.filter(
                Question.id.in_(questoes_ids)).all()

            if questoes:
                exame.questoes = questoes

                # Salvar o exame no banco de dados
                db.session.add(exame)
                db.session.commit()

                return {'message': 'Exame criado com sucesso!'}, 201
            else:
                return {
                    'message':
                    'Alguma(s) questão(ões) não foi(ram) encontrada(s)'
                }, 404
        else:
            return {'message': 'Dados inválidos'}, 400
