from flask_jwt_extended import create_access_token, decode_token as jwt_decode_token

def generate_token(identity, additional_claims=None):
    return create_access_token(identity=identity, additional_claims=additional_claims or {})

def decode_token(token):
    return jwt_decode_token(token)
