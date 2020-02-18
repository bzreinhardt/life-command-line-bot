import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    BOT_NAME = "@lifecommandline_bot"
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    URL = os.environ['BOT_URL']
    TOKEN = os.environ['BOT_TOKEN']
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
    LIST_OF_PROJECTS = [
    'Do a deep dive into the different attempts at algorithmic knowledge generation',
    'Create a database of all the research happening in the world',
    'Create a database of “constraint numbers” that are crossover points between one way of doing technology and another',
    'Look at areas where atom-things are starting to look more like software, identify gaps in that process',
    'Build a map of how innovations are funded now and in the past',
    'Build a map of how innovation organizations are structured now and in the past',
    'Write a manifesto about unbundling the university',
    'Dig into people trying different models',
    'Do a study of the most valuable IP, the research that led to it, the people that did it, and see if you can pattern match against that',
    'Dig through old hype cycles to see possibilities',
    'Do an exploratory project with the large companies with lowest R&D spend that seem like pillars of the economy',
    'Overview of Material Science Breakthroughs that Unlocked other Breakthroughs',
    'Do a survey overview of TTO offices',
    'Pick a starting theme and dig into all the possible quantum leaps that aren’t happening there but could',
    'Map climate as a theme and the possible ecosystem around it',
    'Dig into what defense contractors are doing',
    'Ask VCs to send things that are too crazy or sci fi',
    'Go through current list of Grant calls and see if there’s a way to encode them',
    'Collect and generate positive sci-fi visions and encode their enabling technology',
    'Do a series of digital unconferences around different topics'
    ]
    CUTOFF_VALUE = 75

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
