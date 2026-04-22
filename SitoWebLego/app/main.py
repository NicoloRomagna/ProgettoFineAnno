from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app import db
from app.models import Lego

main = Blueprint('main', __name__)

@main.route('/')
def index():
    legos = Lego.query.all()
    return render_template('index.html', legos=legos)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/aggiungi', methods=['GET', 'POST'])
@login_required
def aggiungi_lego():

    if request.method == 'POST':

        nome = request.form.get('name')
        numero_set = request.form.get('set_number')
        pezzi = request.form.get('pieces')
        anno = request.form.get('year')
        descrizione = request.form.get('description')
        immagine = request.form.get('image_url')
        
        if not nome or not numero_set:
            return "Errore: Nome e Numero Set sono obbligatori", 400

        lego = Lego(
            name=nome,
            set_number=numero_set,
            pieces=int(pezzi) if pezzi else None,
            year=int(anno) if anno else None,
            description=descrizione,
            image=immagine,
            owner_id=current_user.id
        )

        db.session.add(lego)
        db.session.commit()

        return redirect(url_for('main.dashboard'))

    return render_template('aggiungilego.html')


@main.route('/dashboard')
@login_required
def dashboard():

    legos = Lego.query.filter_by(owner_id=current_user.id).all()

    return render_template(
        'dashboard.html',
        user=current_user.username,
        legos=legos
    )