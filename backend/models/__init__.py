from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .item import Item
from .question import Question
from .exame import Exame