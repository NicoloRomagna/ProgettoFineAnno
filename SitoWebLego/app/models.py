from flask_login import UserMixin
from app import db
from datetime import datetime


class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    legos = db.relationship('Lego', backref='owner', lazy=True)


class Lego(db.Model):
    __tablename__ = "lego"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)
    set_number = db.Column(db.String(50), nullable=False)

    pieces = db.Column(db.Integer)
    year = db.Column(db.Integer)

    description = db.Column(db.Text)
    image = db.Column(db.String(255))

    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)