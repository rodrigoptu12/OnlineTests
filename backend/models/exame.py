from . import db


class Exame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    inicio = db.Column(db.DateTime, nullable=False)
    fim = db.Column(db.DateTime)
    estado = db.Column(db.String(50), nullable=False, default='agendado')
    professor_id = db.Column(
        db.Integer, db.ForeignKey('user.userId'), nullable=False)
    questoes = db.relationship('Question', backref='exame', lazy=True)
    respostas = db.relationship('Resposta', backref='exame', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'inicio': self.inicio.isoformat(),
            'fim': self.fim.isoformat() if self.fim else None,
            'estado': self.estado,
            'professor_id': self.professor_id,
        }
