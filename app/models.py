from app import app, db
import datetime

class EventsMeta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(600), nullable=False) # Max 600 characters
    tagline = db.Column(db.String(200)) # Max 200 characters
    cat = db.Column(db.Integer, nullable=False, db.Foreignkey('events_cat.id'))
    organiser = db.Column(db.String(20), nullable=False)
    

class EventsCat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    desc = db.Column(db.Text)