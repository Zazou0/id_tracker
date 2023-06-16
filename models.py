# Import de SQLAlchemy pour gérer la base de données
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


# Initialisation de l'objet SQLAlchemy
db = SQLAlchemy()

# Définition du modèle User pour la table 'user'
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Chaque utilisateur a un ID unique
    username = db.Column(db.String(64), unique=True, nullable=False)  # Le nom d'utilisateur doit être unique et non nul
    password = db.Column(db.String(128), nullable=False)  # Le mot de passe ne doit pas être nul

# Définition du modèle Car pour la table 'car'
class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Chaque voiture a un ID unique
    license_plate = db.Column(db.String(64), unique=True, nullable=False)  # La plaque d'immatriculation doit être unique et non nulle
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Chaque voiture est associée à un utilisateur par le biais d'une clé étrangère
