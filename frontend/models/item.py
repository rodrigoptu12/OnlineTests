from . import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500))
    question_id = db.Column(db.Integer,
                            db.ForeignKey('question.id'),
                            nullable=False)
