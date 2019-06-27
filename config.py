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
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'motham-padithamaanallooo'
    MAIL_SERVER = ''
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    MAIL_DEFAULT_SENDER = ''
    MAIL_MAX_EMAILS = 10000
    HOST_LOC = 'development'
    DEVELOPMENT = True
    DEBUG = True
    JSON_SORT_KEYS = False

class TestingConfig(Config):
    TESTING = True
