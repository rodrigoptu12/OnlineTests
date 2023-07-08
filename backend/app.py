from flask import Flask, render_template, request, redirect, session, jsonify
from flask_restful import Api
from controllers.question_controller import QuestionController
from controllers.user_controller import user_bp

from controllers.exame_controller import ExameController
from dotenv import load_dotenv
from models import db
import pyrebase
import os

load_dotenv()

app = Flask(__name__)


@app.before_request
def reset_session():
    session.pop('user_id', None)


api = Api(app)  # 'app' é a sua instância do aplicativo Flask
api.add_resource(QuestionController, '/questions')
api.add_resource(ExameController, '/exame', '/exame/<int:exame_id>')
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


@app.route('/', methods=['POST', 'GET'])
def index():
    with app.app_context():
        db.create_all()
    if ("user" in session):
        print(session['user'])
        return render_template('home.html', email=session['user']['email'])
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = user
            usuario_existente = Usuario.query.filter_by(email=email).first()
            if usuario_existente:
                return redirect('/')
            else:
                novo_usuario = Usuario(nome=email, email=email)
                db.session.add(novo_usuario)
                db.session.commit()
            return redirect('/')
        except:
            return "Invalid email or password"
    return render_template('login.html')


# criar conta
@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if ("user" in session):
        return render_template('home.html', email=session['user']['email'])
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.create_user_with_email_and_password(email, password)
            # session['user'] = user
            return redirect('/')
        except:
            return "Invalid email or password"
    return render_template('signup.html')


@app.route('/logout')
def logout():
    if ("user" not in session):
        return redirect('/')
    session.pop('user')
    return redirect('/')


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f'<Usuario {self.nome}>'


@app.route('/adicionar_usuario', methods=['POST'])
def adicionar_usuario():
    nome = request.form['nome']
    email = request.form['email']
    novo_usuario = Usuario(nome=nome, email=email)
    db.session.add(novo_usuario)
    db.session.commit()
    return f'Usuário {nome} adicionado com sucesso'


@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = Usuario.query.all()
    usuarios_json = []
    for usuario in usuarios:
        usuario_json = {
            'id': usuario.id,
            'nome': usuario.nome,
            'email': usuario.email
        }
        usuarios_json.append(usuario_json)
    return jsonify(usuarios_json)


if __name__ == '__main__':
    app.run(debug=True)
