from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app import db
from app.models import Lego

main = Blueprint('main', __name__)

@main.route('/')
def index():
    legos = Lego.query.all()
    return render_template('index.html', legos=legos)

@main.route('/dashboard')
@login_required
def dashboard():
    legos = Lego.query.filter_by(owner_id=current_user.id).all()
    return render_template('dashboard.html', legos=legos)

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
            return "Nome e Set obbligatori", 400

        esistente = Lego.query.filter_by(
            set_number=numero_set,
            owner_id=current_user.id
        ).first()

        if esistente:
            return "Set già presente", 400

        try:
            pezzi = int(pezzi) if pezzi else None
            anno = int(anno) if anno else None
        except ValueError:
            return "Pezzi e anno devono essere numeri", 400

        lego = Lego(
            name=nome,
            set_number=numero_set,
            pieces=pezzi,
            year=anno,
            description=descrizione,
            image=immagine,
            owner_id=current_user.id
        )

        db.session.add(lego)
        db.session.commit()

        return redirect(url_for('main.dashboard'))

    return render_template('aggiungilego.html')

@main.route('/edit_lego/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_lego(id):

    lego = Lego.query.filter_by(
        id=id,
        owner_id=current_user.id
    ).first_or_404()

    if request.method == 'POST':

        lego.name = request.form.get('name')
        lego.set_number = request.form.get('set_number')
        lego.description = request.form.get('description')
        lego.image = request.form.get('image_url')

        try:
            lego.pieces = int(request.form.get('pieces')) if request.form.get('pieces') else None
            lego.year = int(request.form.get('year')) if request.form.get('year') else None
        except ValueError:
            pass

        db.session.commit()

        return redirect(url_for('main.dashboard'))

    return render_template('edit_lego.html', lego=lego)

@main.route('/delete_lego/<int:id>', methods=['POST'])
@login_required
def delete_lego(id):

    lego = Lego.query.filter_by(
        id=id,
        owner_id=current_user.id
    ).first_or_404()

    db.session.delete(lego)
    db.session.commit()

    return redirect(url_for('main.dashboard'))

@main.route('/about')
def about():
    return render_template('about.html')