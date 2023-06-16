from werkzeug.security import generate_password_hash
from flask import Flask
from models import db, User, Car

# Créez une instance de l'application Flask, si elle n'existe pas déjà
app = Flask(__name__)

# Configurer l'URI de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'  # Remplacez 'yourdatabase.db' par le nom de votre fichier de base de données
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialiser l'objet db avec l'application
db.init_app(app)

with app.app_context():
    # Récupérer tous les utilisateurs
    users = User.query.all()

    for user in users:
        # Hacher le mot de passe actuel de l'utilisateur
        password_hash = generate_password_hash(user.password)

        # Mettre à jour le mot de passe de l'utilisateur avec le hachage
        user.password = password_hash

        # Enregistrer les modifications dans la base de données
        db.session.commit()
