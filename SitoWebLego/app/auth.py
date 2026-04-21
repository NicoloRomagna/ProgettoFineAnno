from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
from app import db
from app.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash("Compila tutti i campi")
            return redirect(url_for('auth.register'))

        existing = User.query.filter_by(username=username).first()
        if existing:
            flash("Username già esistente")
            return redirect(url_for('auth.register'))

        hashed = generate_password_hash(password)
        user = User(username=username, password=hashed)

        db.session.add(user)
        db.session.commit()

        flash("Registrazione completata")
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password, password):
            flash("Credenziali non valide")
            return redirect(url_for('auth.login'))

        login_user(user)
        return redirect(url_for('main.dashboard'))

    return render_template('auth/login.html')

@bp.route('/logout', methods=['POST'])
def logout():
    from flask_login import logout_user
    logout_user()
    flash("Sei uscito")
    return redirect(url_for('auth.login'))