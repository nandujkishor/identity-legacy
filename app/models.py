from app import app, db
import datetime

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, start=100000000)
    typ = db.Column(db.Integer)
    # User type: Student, Staff, Service account ...
    accesstoken = db.Column(db.String(100))

class Students(db.Model):
    campus = db.Column(db.String(5))
    # AM, BL, CB, ...
    school = db.Column(db.String(5))
    # EN, BT, ...
    program = db.Column(db.String(5))
    # Undergraduate, ...
    name = db.Column(db.String(60))
    gradyear = db.Column(db.Date)

class Staff(db.Model):
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

class ClientApps(db.Model):
    id = db.Column(db.Integer, primary_key=True)
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

class Accesslogs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer)