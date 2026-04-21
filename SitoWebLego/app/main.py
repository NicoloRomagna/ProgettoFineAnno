from flask import Blueprint, render_template, session, redirect, url_for
from app.repositories.lego_repository import LegoRepository

main = Blueprint('main', __name__)

@main.route('/')
def index():
    lego_repo = LegoRepository()
    legos = lego_repo.get_all()
    return render_template('index.html', legos=legos)

@main.route('/aggiungi', methods=['GET', 'POST'])
def aggiungi_lego():
    if 'user' not in session:
        return redirect(url_for('auth.login'))

    from flask import request

    if request.method == 'POST':
        nome = request.form['nome']
        descrizione = request.form['descrizione']

        lego_repo = LegoRepository()
        lego_repo.add(nome, descrizione)

        return redirect(url_for('main.dashboard'))

    return render_template('aggiungilego.html')


@main.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('auth.login'))

    return render_template('dashboard.html', user=session['user'])