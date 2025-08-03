from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user import User
from app.schemas.user_schema import user_schema

user_bp = Blueprint('user', __name__)

@user_bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    uid = get_jwt_identity()['id']
    user = User.query.get_or_404(uid)
    return user_schema.dump(user), 200
