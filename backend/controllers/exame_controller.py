from flask import request
from models import Exame, Question, Resposta
from database.database import db
from flask_restful import Resource
from datetime import datetime
from models.user import User


class ExameController(Resource):

    def get(self, exame_id=None, aluno_id=None):
        data_hora_atual = datetime.now()
        questoes_json = []

        if exame_id:
            exame = Exame.query.get(exame_id)
            respostas = Resposta.query.filter_by(exame_id=exame_id, aluno_id=aluno_id).first()
            if exame:
                if exame.inicio <= data_hora_atual <= exame.fim and not respostas:
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
                        }
                        questoes_json.append(questao_data)
            if questoes_json:
                return questoes_json, 200
            else:
                return {'message': 'Nenhum exame encontrado ou não está disponível para responder'}, 404
        else:
            exames = Exame.query.all()
            exames_json = []
            for exame in exames:
                exame_data = {
                    'id': exame.id,
                    'titulo': exame.titulo,
                    'inicio': exame.inicio.strftime("%Y-%m-%d %H:%M:%S"),
                    'fim': exame.fim.strftime("%Y-%m-%d %H:%M:%S"),
                    'estado': '',
                    'professor': User.query.filter_by(userId=exame.professor_id).first().name,
                }
                if exame.inicio <= data_hora_atual <= exame.fim:
                    exame_data['estado'] = 'Em andamento'
                elif data_hora_atual < exame.inicio:
                    exame_data['estado'] = 'Não aberto'
                else:
                    exame_data['estado'] = 'Finalizado'

                exames_json.append(exame_data)

            return exames_json, 200

    def post(self):
        data = request.get_json()

        titulo = data.get('titulo')
        questoes_ids = data.get('questoes')
        professor_id = data.get('professor_id')
        inicio = data.get('inicio')
        fim = data.get('fim')
        estado = data.get('estado')

        if titulo and questoes_ids and professor_id and inicio and fim and estado:
            # Converter a data de início e fim de string para objeto datetime
            inicio_sem_t = inicio.replace('T', ' ')
            inicio = datetime.strptime(inicio_sem_t, '%Y-%m-%d %H:%M')

            fim_sem_t = fim.replace('T', ' ')
            fim = datetime.strptime(fim_sem_t, '%Y-%m-%d %H:%M')

            exame = Exame(titulo=titulo,
                          professor_id=professor_id,
                          inicio=inicio,
                          fim=fim,
                          estado=estado)

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

    def patch(self, exame_id):
        data = request.get_json()

        titulo = data.get('titulo')
        questoes_ids = data.get('questoes')
        professor_id = data.get('professor_id')
        inicio = data.get('inicio')
        fim = data.get('fim')
        estado = data.get('estado')

        if titulo and questoes_ids and professor_id and inicio and fim and estado:
            # Converter a data de início e fim de string para objeto datetime
            inicio_sem_t = inicio.replace('T', ' ')
            inicio = datetime.strptime(inicio_sem_t, '%Y-%m-%d %H:%M')

            fim_sem_t = fim.replace('T', ' ')
            fim = datetime.strptime(fim_sem_t, '%Y-%m-%d %H:%M')

            exame = Exame.query.get(exame_id)

            if exame:
                exame.titulo = titulo
                exame.professor_id = professor_id
                exame.inicio = inicio
                exame.fim = fim
                exame.estado = estado

                # Buscar as questões existentes pelo ID no banco de dados
                questoes = Question.query.filter(
                    Question.id.in_(questoes_ids)).all()

                if questoes:
                    exame.questoes = questoes

                    # Salvar o exame no banco de dados
                    db.session.commit()

                    return {'message': 'Exame atualizado com sucesso!'}, 200
                else:
                    return {
                        'message':
                        'Alguma(s) questão(ões) não foi(ram) encontrada(s)'
                    }, 404
            else:
                return {'message': 'Exame não encontrado'}, 404
        else:
            return {'message': 'Dados inválidos'}, 400