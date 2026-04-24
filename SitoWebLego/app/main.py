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

        lego = Lego(
            name=request.form.get('name'),
            set_number=request.form.get('set_number'),
            pieces=int(request.form.get('pieces') or 0),
            year=int(request.form.get('year') or 0),
            description=request.form.get('description'),
            image=request.form.get('image_url'),
            color=request.form.get('color'),
            category=request.form.get('category'),
            owner_id=current_user.id
        )

        db.session.add(lego)
        db.session.commit()

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
    legos = Lego.query.all()
    return render_template('catalogo.html', legos=legos)


@main.route('/colore/<colore>')
def colore(colore):
    legos = Lego.query.filter_by(color=colore).all()
    return render_template('catalogo.html', legos=legos, filtro=colore)


@main.route('/categoria/<categoria>')
def categoria(categoria):
    legos = Lego.query.filter_by(category=categoria).all()
    return render_template('catalogo.html', legos=legos, filtro=categoria)


@main.route('/about')
def about():
    return render_template('about.html')