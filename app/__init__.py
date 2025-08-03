from flask import Flask
from .config import Config
from .extensions import db, jwt, migrate, ma
from .routes import register_blueprints

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    ma.init_app(app)

    # Register all route blueprints
    register_blueprints(app)

    return app
