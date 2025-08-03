from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.extensions import db
from app.models.cart import CartItem

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/', methods=['GET'])
@jwt_required()
def show():
    uid = get_jwt_identity()['id']
    items = CartItem.query.filter_by(user_id=uid).all()
    return jsonify([{'product_id': i.product_id, 'quantity': i.quantity, 'id': i.id} for i in items]), 200

@cart_bp.route('/', methods=['POST'])
@jwt_required()
def add():
    data = request.get_json()
    uid = get_jwt_identity()['id']
    item = CartItem.query.filter_by(user_id=uid, product_id=data['product_id']).first()
    if item:
        item.quantity += data.get('quantity', 1)
    else:
        item = CartItem(user_id=uid, product_id=data['product_id'], quantity=data.get('quantity',1))
        db.session.add(item)
    db.session.commit()
    return jsonify({'message':'Added'}), 201

@cart_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def remove(id):
    uid = get_jwt_identity()['id']
    item = CartItem.query.filter_by(id=id, user_id=uid).first_or_404()
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message':'Removed'}), 200
