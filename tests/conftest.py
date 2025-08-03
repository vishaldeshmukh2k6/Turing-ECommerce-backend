import pytest
from app import create_app
from app.extensions import db
from flask_jwt_extended import create_access_token

@pytest.fixture
def app():
    app = create_app(testing=True)
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def user_token():
    return create_access_token(identity="user@example.com", additional_claims={"role": "user"})

@pytest.fixture
def admin_token():
    return create_access_token(identity="admin@example.com", additional_claims={"role": "admin"})

@pytest.fixture
def user_headers(user_token):
    return {"Authorization": f"Bearer {user_token}"}

@pytest.fixture
def admin_headers(admin_token):
    return {"Authorization": f"Bearer {admin_token}"}
