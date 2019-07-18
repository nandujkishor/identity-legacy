from flask import Flask
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
from app import app

class Token(object):
    def __init__(self, id, username):
        