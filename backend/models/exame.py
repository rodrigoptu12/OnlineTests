from .resposta import Resposta
from . import db


class Exame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    inicio = db.Column(db.DateTime, nullable=False)
    fim = db.Column(db.DateTime)
    estado = db.Column(db.String(50), nullable=False, default='agendado')
    professor_id = db.Column(db.Integer,
                             db.ForeignKey('user.userId'),
                             nullable=False)
    questoes = db.relationship('Question', backref='exame', lazy=True)
    respostas = db.relationship('Resposta', backref='exame', lazy=True)
    professor = db.relationship('User',
                                backref=db.backref('exames', lazy=True))
