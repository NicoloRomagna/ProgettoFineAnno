from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.repositories.user_repository import UserRepository
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user_repo = UserRepository()
        user = user_repo.get_by_username(username)

        if user and check_password_hash(user['password'], password):
            session['user'] = username
            return redirect(url_for('main.dashboard'))
        else:
            flash("Credenziali non valide")

    return render_template('auth/login.html')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])

        user_repo = UserRepository()
        user_repo.create(username, password)

        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')


@auth.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('main.index'))