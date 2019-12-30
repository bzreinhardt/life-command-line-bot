import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MIGRATION_DIR = os.path.join(basedir, 'migrations')
    FIREBASE_CREDENTIALS=os.path.join(basedir, 'serviceAccount.json')
    FIREBASE_DUMP=os.path.join(basedir, 'db.json')
    FIREBASE_API_KEY="<your api key>"
    FIREBASE_AUTH_DOMAIN = "now-pages.firebaseapp.com"
    FIREBASE_PROJECT_ID = "now-pages"
    FIREBASE_AUTH_SIGN_IN_OPTIONS = "google, twitter"
    BCRYPT_LOG_ROUNDS = 13

class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4


class TestingConfig(Config):
    TESTING = True
