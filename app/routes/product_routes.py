from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.extensions import db
from app.models.product import Product
from app.schemas.product_schema import product_schema, products_schema

product_bp = Blueprint('products', __name__)

@product_bp.route('/', methods=['GET'])
def all_products():
    return products_schema.dump(Product.query.all()), 200

@product_bp.route('/<int:id>', methods=['GET'])
def one_product(id):
    return product_schema.dump(Product.query.get_or_404(id)), 200

@product_bp.route('/', methods=['POST'])
@jwt_required()
def create():
    data = request.get_json()
    p = Product(name=data['name'], description=data.get('description', ''),
                price=data['price'], stock=data['stock'])
    db.session.add(p)
    db.session.commit()
    return product_schema.dump(p), 201

@product_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update(id):
    p = Product.query.get_or_404(id)
    data = request.get_json()
    for key in ['name','description','price','stock']:
        if key in data:
            setattr(p, key, data[key])
    db.session.commit()
    return product_schema.dump(p), 200

@product_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    p = Product.query.get_or_404(id)
    db.session.delete(p)
    db.session.commit()
    return {'message':'Deleted'}, 200
