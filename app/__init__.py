from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import firebase_admin
from firebase_admin import credentials

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
cred = credentials.Certificate(app.config['FIREBASE_CREDENTIALS'])
firebase_admin.initialize_app(cred)

from app import routes, models
