from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    userId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    registration = db.Column(db.Integer, nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    is_teacher = db.Column(db.Boolean, default=False)
    assigned_exames = db.relationship('Exame',
                                      backref=db.backref('assigned_professor',
                                                         lazy=True),
                                      primaryjoin="User.userId == "
                                      "Exame.professor_id")

    def serialize(self):
        return {
            'id': self.userId,
            'name': self.name,
            'email': self.email,
            'registration': self.registration,
            'is_teacher': self.is_teacher,
            'exames': self.exames
        }

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        if len(password) < 8:
            raise ValueError('Password must be at least 8 characters long.')
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
