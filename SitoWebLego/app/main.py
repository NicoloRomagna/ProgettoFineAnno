from flask import Blueprint, render_template, request, redirect, url_for, flash
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

        name = request.form.get('name')
        set_number = request.form.get('set_number')
        pieces = int(request.form.get('pieces') or 0)
        year = int(request.form.get('year') or 0)
        description = request.form.get('description')
        image = request.form.get('image_url')
        color = request.form.get('color')
        price = float(request.form.get('price') or 0)
        is_minifigure = request.form.get("is_minifigure") == "1"
        is_botanica = request.form.get("is_botanica") == "1"

        lego_esistente = Lego.query.filter_by(
            set_number=set_number,
            owner_id=current_user.id
        ).first()

        if lego_esistente:
            flash("Questo set LEGO è già presente nella tua collezione", "danger")
            return redirect(url_for('main.aggiungi_lego'))

        lego = Lego(
            name=name,
            set_number=set_number,
            pieces=pieces,
            year=year,
            description=description,
            image=image,
            owner_id=current_user.id,
            is_minifigure=is_minifigure,
            is_botanica=is_botanica,
            color=color,
            price=price
        )

        db.session.add(lego)
        db.session.commit()

        flash("Set aggiunto", "success")
        return redirect(url_for('main.dashboard'))

    return render_template('aggiungilego.html')

@main.route('/edit_lego/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_lego(id):
    lego = Lego.query.get_or_404(id)

    if request.method == 'POST':
        lego.name = request.form.get('name')
        lego.set_number = request.form.get('set_number')
        lego.pieces = request.form.get('pieces') or None
        lego.year = request.form.get('year') or None
        lego.description = request.form.get('description')
        lego.image = request.form.get('image_url')
        lego.color = request.form.get('color')
        lego.price = float(request.form.get('price') or 0)
        lego.is_minifigure = request.form.get("is_minifigure") == "1"
        lego.is_botanica = request.form.get("is_botanica") == "1"

        db.session.commit()

        flash("Modifiche salvate!", "success")
        return redirect(url_for('main.dashboard'))

    return render_template('edit_lego.html', lego=lego)

@main.route('/delete_lego/<int:id>', methods=['POST'])
@login_required
def delete_lego(id):

    lego = Lego.query.filter_by(id=id, owner_id=current_user.id).first_or_404()

    db.session.delete(lego)
    db.session.commit()

    return redirect(url_for('main.dashboard'))

@main.route('/catalogo')
def catalogo():
    return render_template('catalogo.html')


@main.route('/colore_dettaglio/<colore>')
@login_required
def colore_dettaglio(colore):

    prezzi = {
        "bordeaux": 0.30,
        "rosso": 0.25,
        "arancione": 0.45,
        "giallo": 0.20,
        "verde chiaro": 0.35,
        "verde": 0.50,
        "azzurro chiaro": 0.70,
        "azzurro": 0.40,
        "blu": 0.55,
        "viola": 0.60,
        "lavanda": 0.65,
        "fucsia": 0.35,
        "rosa": 0.25,
        "beige": 0.20,
        "marrone": 0.45,
        "nero": 0.05,
        "grigio": 0.25,
        "grigio chiaro": 0.35,
        "bianco": 0.10,
        "trasparente": 0.85
    }


    legos = Lego.query.filter_by(
        owner_id=current_user.id,
        color=colore
    ).all()

    return render_template(
        "colore_dettaglio.html",
        colore=colore,
        prezzo=prezzi.get(colore, 0),
        legos=legos
    )


@main.route('/minifigures_dettaglio')
@login_required
def minifigures_dettaglio():

    prezzo = 1.50

    minifigs = Lego.query.filter_by(
        owner_id=current_user.id,
        is_minifigure=True
    ).all()

    return render_template(
        "minifigures_dettaglio.html",
        prezzo=prezzo,
        minifigs=minifigs
    )


@main.route('/botanica_dettaglio')
@login_required
def botanica_dettaglio():

    prezzi = {
        "albero": 0.50,
        "fiori": 0.10,
        "foglie": 0.30,
        "cespuglio": 0.40
    }

    botanica = Lego.query.filter_by(
        owner_id=current_user.id,
        is_botanica=True
    ).all()

    return render_template(
        "botanica_dettaglio.html",
        prezzi=prezzi,
        botanica=botanica
    )

@main.route('/about')
def about():
    return render_template('about.html')
