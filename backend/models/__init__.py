from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .exame import Exame
from .question import Question
from .exame import Exame