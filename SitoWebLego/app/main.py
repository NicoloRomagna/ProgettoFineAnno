from flask import Flask, render_template, redirect, url_for, request, flash, abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"

# -------- MODELS --------
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Lego(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    set_number = db.Column(db.String(50), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

# -------- REGISTER --------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash("Compila tutti i campi")
            return redirect(url_for('register'))

        existing = User.query.filter_by(username=username).first()
        if existing:
            flash("Username già esistente")
            return redirect(url_for('register'))

        hashed = generate_password_hash(password)
        user = User(username=username, password=hashed)

        db.session.add(user)
        db.session.commit()

        flash("Registrazione completata")
        return redirect(url_for('login'))

    return render_template('register.html')

# -------- LOGIN --------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password, password):
            flash("Credenziali non valide")
            return redirect(url_for('login'))

        login_user(user)
        return redirect(url_for('dashboard'))

    return render_template('login.html')

# -------- LOGOUT (POST) --------
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    flash("Sei uscito")
    return redirect(url_for('login'))

# -------- DASHBOARD --------
@app.route('/', methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        name = request.form.get('name')
        set_number = request.form.get('set_number')

        if not name or not set_number:
            flash("Compila tutti i campi")
            return redirect(url_for('dashboard'))

        # evita duplicati
        existing = Lego.query.filter_by(
            set_number=set_number,
            owner_id=current_user.id
        ).first()

        if existing:
            flash("Questo LEGO è già presente!")
        else:
            lego = Lego(
                name=name,
                set_number=set_number,
                owner_id=current_user.id
            )
            db.session.add(lego)
            db.session.commit()
            flash("LEGO aggiunto!")

        return redirect(url_for('dashboard'))

    legos = Lego.query.filter_by(owner_id=current_user.id).all()
    return render_template('dashboard.html', legos=legos)

# -------- DELETE (POST) --------
@app.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete_lego(id):
    lego = Lego.query.get_or_404(id)

    if lego.owner_id != current_user.id:
        abort(403)

    db.session.delete(lego)
    db.session.commit()
    flash("LEGO eliminato")
    return redirect(url_for('dashboard'))

# -------- INIT DB --------
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)