from app import db
from sqlalchemy.dialects.postgresql import JSON
from flask_login import UserMixin
import datetime


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    social_id = db.Column(db.String(), nullable=False, unique=True)
    nickname = db.Column(db.String(), nullable=True)
    email = db.Column(db.String(), nullable=True)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    picture = db.Column(db.String(), nullable=True)
    name = db.Column(db.String(), nullable=True)

    def __init__(self, social_id,
                picture=None,
                name = None,
                email = None,
                admin=False):
        self.social_id = social_id
        self.picture = picture
        self.name = name
        self.email = email
        self.registered_on = datetime.datetime.now()
        self.admin = admin

class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    raw_text = db.Column(db.String(), nullable=True)
    received = db.Column(db.DateTime, nullable=False)

    def __init__(self, raw_text):
        self.raw_text = raw_text
        self.received = datetime.datetime.now()

class KPI(db.Model):
    __tablename__ = 'kpis'
    id = db.Column(db.Integer, primary_key=True)
    received = db.Column(db.DateTime, nullable=False)
    type = db.Column(db.String(), nullable=False)
    value = db.Column(db.String(), nullable=True)

    def __init__(self, type, value):
        self.type = type
        self.value = value
        self.received = datetime.datetime.now()
