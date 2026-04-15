from flask import Blueprint, render_template, request, redirect, url_for
from .repositories.lego_repository import get_all_lego, add_lego

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    legos = get_all_lego()
    return render_template('index.html', legos=legos)

@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        image = request.form['image']

        add_lego(name, description, image)
        return redirect(url_for('main.index'))

    return render_template('crealego.html')