from .auth_routes import auth_bp
from .user_routes import user_bp
from .product_routes import product_bp
from .cart_routes import cart_bp
from .order_routes import order_bp
from .admin_routes import admin_bp

def register_blueprints(app):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(product_bp, url_prefix='/products')
    app.register_blueprint(cart_bp, url_prefix='/cart')
    app.register_blueprint(order_bp, url_prefix='/orders')
    app.register_blueprint(admin_bp, url_prefix='/admin')
