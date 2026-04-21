from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret123'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    
    # Inizializza estensioni
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'  # CORRETTO: usa il blueprint endpoint
    
    # Registra blueprints
    from app.auth import bp as auth_bp
    from app.main import bp as main_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    
    # Context processor per login_manager
    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User
        return db.session.get(User, int(user_id))
    
    # Crea tabelle
    with app.app_context():
        db.create_all()
    
    return app