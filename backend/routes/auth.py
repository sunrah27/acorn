from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from .db import get_users_collection

auth_bp = Blueprint('auth', __name__)

# Login route
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    users_collection = get_users_collection
    user = users_collection.find_one({"email": email})

    if user and check_password_hash(user['password']):
        token = jwt.encode({
            'user_id': str(user['_id']),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
        }, 'your_secret_key', algorithm='HS256')

        return jsonify({'success': True, 'token': token}), 200
    return jsonify({'success': False, 'message': 'Invalid email or password'}), 401