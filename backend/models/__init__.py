from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .exame import Exame
from .question import Question
from .exame import Exame
from .user import User
from .item import Item
from .resposta import Resposta