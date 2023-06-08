from flask import Flask
from models import db, User, Car

# Configuration de l'application Flask (nécessaire pour SQLAlchemy)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialisation de SQLAlchemy avec l'application Flask
db.init_app(app)

# Création de toutes les tables
with app.app_context():
    db.create_all()

# Création d'un nouvel utilisateur
with app.app_context():
    new_user = User(username='test', password='test')
    db.session.add(new_user)
    db.session.commit()

# Récupération de tous les utilisateurs
with app.app_context():
    users = User.query.all()
    for user in users:
        print(user.username)
