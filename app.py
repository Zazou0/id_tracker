# Importation des modules nécessaires de Flask
from flask import Flask, request, session, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Création d'une nouvelle application Flask
app = Flask(__name__)

# Configuration de l'application pour utiliser une base de données SQLite locale
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'votre_clé_secrète_générée_aléatoirement'

# Initialisation de l'objet SQLAlchemy
db = SQLAlchemy(app)

# Définition du modèle User pour la table 'user'
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# Définition du modèle Car pour la table 'car'
class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    license_plate = db.Column(db.String(64), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Création de toutes les tables de la base de données (si elles n'existent pas déjà)
with app.app_context():
    db.create_all()

@app.route('/create_test_user', methods=['GET'])
def create_test_user():
    # Création d'un nouvel utilisateur
    new_user = User(username='test', password='test')
    db.session.add(new_user)
    db.session.commit()
    
    return "Test user created successfully"

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None  # Variable pour stocker le message d'erreur

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user is None:
            error = "L'utilisateur n'existe pas"
        elif user.password != password:
            error = "Le mot de passe est incorrect"
        else:
            session['username'] = username
            return redirect(url_for('index'))  # Redirige l'utilisateur vers la fonction qui gère la route /account
    
    return render_template('login.html', error=error)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', session=session)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return "User logged out successfully"

@app.route('/account')
def account():
    username = session.get('username')
    
    if username is None:
        return redirect(url_for('login'))
        
    else:
        return render_template('account.html', username=username)


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None  # Variable pour stocker le message d'erreur

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        existing_user = User.query.filter_by(username=username).first()

        if existing_user is not None:
            error = "L'utilisateur existe déjà"
        else:
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))  # Redirige l'utilisateur vers la fonction qui gère la route /login
    
    return render_template('register.html', error=error)


@app.route('/license_plate_recognition')
def license_plate_recognition():
    username = session.get('username')
    
    if username is None:
        return redirect(url_for('login'))
        
    else:
        # code programme plaque immat
        return render_template('license_plate_recognition.html', username=username)


# Si ce module est le fichier principal exécuté, exécutez l'application
if __name__ == "__main__":
    app.run(debug=True)
