from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user import User
from app.models.order import Order

admin_bp = Blueprint('admin', __name__)

def is_admin():
    identity = get_jwt_identity()
    return identity and identity.get('role') == 'admin'

@admin_bp.route('/users', methods=['GET'])
@jwt_required()
def all_users():
    if not is_admin():
        return jsonify({'error': 'Admins only'}), 403
    users = User.query.all()
    return jsonify([{'id': u.id, 'email': u.email, 'role': u.role} for u in users]), 200

@admin_bp.route('/orders', methods=['GET'])
@jwt_required()
def all_orders():
    if not is_admin():
        return jsonify({'error': 'Admins only'}), 403
    orders = Order.query.all()
    return jsonify([{
        'id': o.id,
        'user': o.user_id,
        'total': o.total_price,
        'status': o.status
    } for o in orders]), 200
