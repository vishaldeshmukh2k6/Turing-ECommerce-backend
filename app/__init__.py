from flask import Flask
from .config import config_by_name
from .extensions import db, jwt, ma
from .routes import register_blueprints

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    db.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)

    register_blueprints(app)

    @app.route('/')
    def index():
        return {"message": "Welcome to Turing E-Commerce API"}, 200

    return app
