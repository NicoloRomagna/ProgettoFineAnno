from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app import db
from app.models import Lego

main = Blueprint('main', __name__)

@main.route('/')
def index():
    legos = Lego.query.all()
    return render_template('index.html', legos=legos)


@main.route('/aggiungi', methods=['GET', 'POST'])
@login_required
def aggiungi_lego():
    if request.method == 'POST':
        lego = Lego(
            name=request.form['nome'],
            description=request.form['descrizione'],
            image=request.form.get('image')
        )

        db.session.add(lego)
        db.session.commit()

        return redirect(url_for('main.dashboard'))

    return render_template('aggiungilego.html')


@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)