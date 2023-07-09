from flask import Flask
from flask_restful import Api
from controllers.question_controller import QuestionController
from controllers.user_controller import user_bp
from controllers.exame_controller import ExameController
from controllers.resposta_controller import RespostaController
from dotenv import load_dotenv
from models import db
import pyrebase
import os
from flask_cors import CORS


load_dotenv()

app = Flask(__name__)
CORS(app)


@app.before_request
def reset_session():
    session.pop('user_id', None)

api = Api(app)  # 'app' é a sua instância do aplicativo Flask
api.add_resource(QuestionController, '/questions')

api.add_resource(ExameController, '/exame', '/exame/<int:exame_id>')
api.add_resource(RespostaController, '/resposta', '/resposta/<int:id_exame>')
app.register_blueprint(user_bp)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'SQLALCHEMY_DATABASE_URI')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

firebase_api_key = os.getenv("FIREBASE_API_KEY")
firebase_auth_domain = os.getenv("FIREBASE_AUTH_DOMAIN")
firebase_project_id = os.getenv("FIREBASE_PROJECT_ID")
firebase_storage_bucket = os.getenv("FIREBASE_STORAGE_BUCKET")
firebase_messaging_sender_id = os.getenv("FIREBASE_MESSAGING_SENDER_ID")
firebase_app_id = os.getenv("FIREBASE_APP_ID")
firebase_measurement_id = os.getenv("FIREBASE_MEASUREMENT_ID")
firebase_database_url = os.getenv("FIREBASE_DATABASE_URL")

config = {
    "apiKey": firebase_api_key,
    "authDomain": firebase_auth_domain,
    "projectId": firebase_project_id,
    "storageBucket": firebase_storage_bucket,
    "messagingSenderId": firebase_messaging_sender_id,
    "appId": firebase_app_id,
    "measurementId": firebase_measurement_id,
    "databaseURL": firebase_database_url
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app.secret_key = 'secret'

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
