from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.extensions import db
from app.models.order import Order
from app.models.cart import CartItem
from app.models.product import Product

order_bp = Blueprint('orders', __name__)

@order_bp.route('/', methods=['POST'])
@jwt_required()
def place_order():
    uid = get_jwt_identity()['id']
    cart_items = CartItem.query.filter_by(user_id=uid).all()
    if not cart_items:
        return jsonify({'error': 'Cart is empty'}), 400

    total = 0
    for item in cart_items:
        product = Product.query.get(item.product_id)
        if product.stock < item.quantity:
            return jsonify({'error': f'Insufficient stock for {product.name}'}), 400
        total += product.price * item.quantity
        product.stock -= item.quantity

    order = Order(user_id=uid, total_price=total)
    db.session.add(order)
    CartItem.query.filter_by(user_id=uid).delete()
    db.session.commit()

    return jsonify({'message': 'Order placed', 'order_id': order.id}), 201

@order_bp.route('/', methods=['GET'])
@jwt_required()
def list_orders():
    uid = get_jwt_identity()['id']
    orders = Order.query.filter_by(user_id=uid).all()
    return jsonify([{
        'id': o.id,
        'total': o.total_price,
        'status': o.status,
        'created': o.created_at
    } for o in orders]), 200
