from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .repositories.user_repository import create_user, get_user

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])

        try:
            create_user(username, password)
            return redirect(url_for('auth.login'))
        except:
            flash("Utente già esistente")

    return render_template('auth/register.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = get_user(username)

        if user and check_password_hash(user['password'], password):
            return redirect(url_for('main.index'))
        else:
            flash("Credenziali non valide")

    return render_template('auth/login.html')