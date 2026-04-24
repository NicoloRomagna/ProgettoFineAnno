import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret123'

    base_dir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(base_dir, '..', 'instance', 'lego.sqlite')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.abspath(db_path)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from app.auth import auth
    from app.main import main

    app.register_blueprint(auth)
    app.register_blueprint(main)

    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    return app