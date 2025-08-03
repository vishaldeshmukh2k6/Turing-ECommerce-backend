from .extensions import db

def init_db(app):
    with app.app_context():
        db.create_all()
        print(" Database tables created.")

def drop_db(app):
    with app.app_context():
        db.drop_all()
        print(" Database tables dropped.")
