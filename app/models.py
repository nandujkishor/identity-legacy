from app import app, db
import datetime
import jwt

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, start=100000000)
    typ = db.Column(db.Integer)
    # User type: Student, Staff, Guest, Service account ...
    accesstoken = db.Column(db.String(100))
    email = db.Column(db.String(200))

    def __init__(self, typ, accesstoken, email):
        self.typ = typ
        self.accesstoken = accesstoken
        self.email = email
    
    def super(self):
        return self.email == 'nandakishore@am.students.amrita.edu'

    def encode_auth_token(self, id):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=100, seconds=0),
                'iat': datetime.datetime.utcnow(),
                'sub': id
            }
            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e
    
    @staticmethod
    def decode_auth_token(auth_token):
        # Params: JWT
        # Returns: UserID / ErrorID (int)
        try:
            payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            print("Expired token")
            return "Expired token"
            # Signature expired. Need to login again.
        except jwt.InvalidTokenError:
            print("Invalid token")
            return "Invalid token"
            # Invalid token. Need to login again.

class BlacklistToken(db.Model):
    # Token Model for storing JWT tokens
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.Text, unique=True, nullable=False)
    blacklisted_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, token):
        self.token = token
        self.blacklisted_on = datetime.datetime.now()
        print("Blacklisted")

    def __repr__(self):
        return '<id: token: {}'.format(self.token)

    @staticmethod
    def check_blacklist(auth_token):
        # check whether auth token has been blacklisted
        res = BlacklistToken.query.filter_by(token=str(auth_token)).first()
        if res:
            return True
        else:
            return False

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True, db.Foreignkey('users.id'))
    campus = db.Column(db.String(5))
    # AM, BL, CB, ...
    school = db.Column(db.String(5))
    # EN, BT, ...
    program = db.Column(db.String(5))
    # Undergraduate, ...
    name = db.Column(db.String(60))
    gradyear = db.Column(db.Date)

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True, db.Foreignkey('users.id'))
    campus = db.Column(db.String(5))
    dept = db.Column(db.String(5))
    empid = db.Column(db.Integer)

class Organisation(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, start=500000000)
    name = db.Column(db.String(100))

class Orgaccess(db.Model):
    uid = db.Column(db.Integer, primary_key=True, db.Foreignkey('users.id'))
    oid = db.Column(db.Integer, primary_key=True, db.Foreignkey('organisation.id'))
    perm = db.Column(db.Integer)

class ClientApp(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    img = db.Column(db.String(1000))
    secret = db.Column(db.String(100))
    # Hashed
    redirecturl = db.Column(db.String(1000))
    trust = db.Column(db.Integer)
    # 1: Highly trusted application - no scope authorization required
    # (same team)
    # 2: Verified trusted application - user authorization required
    # (shows in the interface application is trusted)
    # 3: Unknown application
    # (show users to make sure their data is not misused)

class AuthCode(db.Model):
    atid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timecr = db.Column(db,Datetime, default=datetime.datetime.utcnow)

class AccessCode(db.Model):
    acid = db.Column(db.Integer, primary_key=True, autoincrement=True)

class Accesslogs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer)