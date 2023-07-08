from . import db


class Resposta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_aluno = db.Column(db.Integer)
    id_exame = db.Column(db.Integer, db.ForeignKey('exame.id'), nullable=False)
    respostas = db.Column(db.JSON)
