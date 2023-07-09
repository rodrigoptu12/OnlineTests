from . import db
from datetime import datetime


class Resposta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_aluno = db.Column(db.Integer)
    id_exame = db.Column(db.Integer, db.ForeignKey('exame.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    respostas = db.Column(db.JSON)
