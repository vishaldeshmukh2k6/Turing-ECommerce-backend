from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from datetime import timedelta
from app.extensions import db
from app.models.user import User
from app.schemas.user_schema import user_schema

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already registered'}), 400
    hashed = generate_password_hash(data['password'])
    user = User(name=data['name'], email=data['email'], password=hashed,
                role=data.get('role', 'customer'))
    db.session.add(user)
    db.session.commit()
    return jsonify(user_schema.dump(user)), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'error': 'Invalid credentials'}), 401
    access = create_access_token(identity={'id': user.id, 'role': user.role},
                                 expires_delta=timedelta(hours=24))
    return jsonify({'token': access, 'user': user_schema.dump(user)}), 200
