from . import db


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    command = db.Column(db.String(1000))
    items = db.relationship('Item', backref='question', lazy=True)
    answer_key = db.Column(db.String(1000))
    question_type = db.Column(db.String(100), nullable=False)
