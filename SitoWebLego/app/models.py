from app import db
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    legos = db.relationship('Lego', backref='owner', lazy=True)


class Lego(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    set_number = db.Column(db.String(20), nullable=False)
    pieces = db.Column(db.Integer)
    year = db.Column(db.Integer)
    description = db.Column(db.Text)
    image = db.Column(db.String(300))
    price = db.Column(db.Float)

    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    color = db.Column(db.String(50))
    is_minifigure = db.Column(db.Boolean, default=False)
    is_botanica = db.Column(db.Boolean, default=False)

