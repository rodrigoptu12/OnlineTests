from flask import Flask
from flask_restful import Api
from controllers.question_controller import QuestionController
from controllers.user_controller import user_bp
from controllers.exame_controller import ExameController
from controllers.resposta_controller import RespostaController
from dotenv import load_dotenv
from models import db
import os
from flask_cors import CORS
from flask_jwt_extended import JWTManager


load_dotenv()

app = Flask(__name__)
CORS(app)
# Chave secreta para assinar os tokens JWT
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
jwt = JWTManager(app)

api = Api(app)  # 'app' é a sua instância do aplicativo Flask
api.add_resource(QuestionController, '/questions')

api.add_resource(ExameController, '/exame', '/exame/<int:exame_id>')
api.add_resource(RespostaController, '/resposta', '/resposta/<int:id_exame>')
app.register_blueprint(user_bp)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'SQLALCHEMY_DATABASE_URI')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


app.secret_key = 'secret'

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
