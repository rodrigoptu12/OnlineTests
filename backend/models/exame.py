from .resposta import Resposta
from . import db


class Exame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    questoes = db.relationship('Question', backref='exame', lazy=True)
    respostas = db.relationship('Resposta', backref='exame', lazy=True)
