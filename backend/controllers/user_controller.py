from flask import request, jsonify, session
from flask_restful import Resource
from decorators.decorators import require_login
from models.user import User
from models import db
from flask import Blueprint
from flask_cors import cross_origin
from flask_jwt_extended import create_access_token, jwt_required
from flask_jwt_extended import get_jwt_identity


user_bp = Blueprint('user', __name__)


class UserController(Resource):
    @staticmethod
    @user_bp.route('/users', methods=['GET'])
    @cross_origin()
    @require_login
    def get_all_users():
        if session.get('user_id') is None:
            return jsonify({'error': 'Login require'}), 404

        user_session = User.query.get(session.get('user_id'))

        if user_session is None or not user_session.is_teacher:
            return jsonify({'error': 'User without permition'}), 404

        users = User.query.all()

        return jsonify([user.serialize() for user in users])

    @staticmethod
    @user_bp.route('/users/<int:user_id>', methods=['GET'])
    @cross_origin()
    @require_login
    def get_user(user_id):
        user = User.query.get(user_id)
        user_session_id = session.get('user_id')
        user_session = User.query.get(session.get(user_session_id))

        if not user_session.is_teacher and not user.userId == user_session_id:
            return jsonify({'message': 'User without permition'})

        if not user:
            return jsonify({'error': 'User not found'}), 404

        return jsonify(user.serialize())

    @staticmethod
    @user_bp.route('/users', methods=['POST'])
    def create_user():
        data = request.json
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        registration = data.get('registration')
        is_teacher = data.get('is_teacher', False)

        if not name:
            return jsonify({'error': 'Name is required'}), 400

        if not email:
            return jsonify({'error': 'Email is required'}), 400

        if not password:
            return jsonify({'error': 'Password is required'}), 400

        if not confirm_password:
            return jsonify({'error': 'Confirm password is required'}), 400

        if not registration:
            return jsonify({'error': 'Registration is required'}), 400

        if not (User.query.filter_by(email=email).first() is None):
            return jsonify({'error': 'Email already registered'}), 400

        if not (User.query.filter_by(registration=registration).first()
                is None):
            return jsonify({'error': 'Registration already registered'}), 400

        if password != confirm_password:
            return jsonify({'error': 'Password and confirm_password '
                            'are diferrent'}), 400

        user = User(name=name, email=email, password=password,
                    registration=registration, is_teacher=is_teacher)

        db.session.add(user)
        db.session.commit()

        return jsonify(user.serialize()), 201

    @staticmethod
    @user_bp.route('/users/<int:user_id>', methods=['PUT'])
    @cross_origin()
    @require_login
    def update_user(user_id):
        user = User.query.get(user_id)
        user_session_id = session.get('user_id')
        user_session = User.query.get(session.get(user_session_id))

        if not user_session.is_teacher and not user.userId == user_session_id:
            return jsonify({'message': 'User without permition'})

        if not user:
            return jsonify({'error': 'User not found'}), 404

        data = request.json
        name = data.get('name')
        email = data.get('email')
        new_email = data.get('new_email')
        password = data.get('password')
        new_password = data.get('new_password')

        if not name:
            return jsonify({'error': 'Name is required'}), 400

        if not email:
            return jsonify({'error': 'Email is required'}), 400

        if not password:
            return jsonify({'error': 'Password is required'}), 400

        if User.query.filter_by(email=email).first() is None:
            return jsonify({'error': 'Email doesnt exist'}), 400

        if not user.verify_password(password):
            return jsonify({'error': 'Wrong password'}), 400

        user.name = name

        if new_email:
            user.email = new_email

        if new_password:
            user.password = new_password

        db.session.commit()

        return jsonify(user.serialize())

    @staticmethod
    @user_bp.route('/users/<int:user_id>', methods=['DELETE'])
    @cross_origin()
    @require_login
    def delete_user(user_id):
        user = User.query.get(user_id)
        user_session_id = session.get('user_id')
        user_session = User.query.get(session.get(user_session_id))

        if not user_session.is_teacher and not user.userId == user_session_id:
            return jsonify({'message': 'User without permition'})

        if not user:
            return jsonify({'error': 'User not found'}), 404

        db.session.delete(user)
        db.session.commit()

        return jsonify({'message': 'User deleted'})

    @staticmethod
    @user_bp.route('/login', methods=['POST'])
    def login():
        data = request.json
        email = data.get('email')
        password = data.get('password')

        if not email:
            return jsonify({'error': 'Email is required'}), 400

        if not password:
            return jsonify({'error': 'Password is required'}), 400

        user = User.query.filter_by(email=email).first()

        if not user or not user.verify_password(password):
            return jsonify({'error': 'Invalid email or password'}), 401

        session.permanent = True

        session['user_id'] = user.userId

        access_token = create_access_token(identity=user.userId)

        return jsonify(access_token=access_token), 200

    @staticmethod
    @user_bp.route('/logout', methods=['POST'])
    @cross_origin()
    @jwt_required()
    def logout():
        """ jti = get_raw_jwt()['jti']
        revoked_tokens.add(jti)  """

        return jsonify({'message': 'Logged out'})

    @staticmethod
    @user_bp.route('/me', methods=['GET'])
    @cross_origin()
    @jwt_required()
    def get_current_user():
        user_id = get_jwt_identity()
        print(user_id)
        if user_id:
            user = User.query.get(user_id)
            if user:
                return jsonify(user.serialize())

        return jsonify({'error': 'Not logged in'}), 401
