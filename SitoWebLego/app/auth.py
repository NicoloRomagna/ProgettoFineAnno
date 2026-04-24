from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user
from app import db
from app.models import User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('main.dashboard'))

        flash("Credenziali non valide")

    return render_template('auth/login.html')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        hashed_pw = generate_password_hash(request.form['password'])

        user = User(
            username=request.form['username'],
            password=hashed_pw
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))