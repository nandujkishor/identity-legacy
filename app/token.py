from app import app
from flask_jwt import JWT, jwt_required, current_identity

jwt = JWT(app, authenticate, identity)

@jwt.identity_handler
def identify(payload):
    return User.query.filter(User.id == payload['identity']).scalar()