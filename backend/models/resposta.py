from . import db
from datetime import datetime


class Resposta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer)
    exame_id = db.Column(db.Integer, db.ForeignKey('exame.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    respostas = db.Column(db.JSON)
