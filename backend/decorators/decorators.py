from functools import wraps
from flask import session, jsonify


def require_login(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({'error': 'Authentication required'}), 401
        return func(*args, **kwargs)
    return decorated
