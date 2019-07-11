import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    POSTGRES = {
        'user': '',
        'pw': '',
        'db': '',
        'host': '',
        'port': '5432',
    }
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASEURL = 'http://localhost:2000'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'motham-padithamaanallooo'
    HOST_LOC = 'development'
    DEVELOPMENT = True
    DEBUG = True
    JSON_SORT_KEYS = False

class TestingConfig(Config):
    TESTING = True
