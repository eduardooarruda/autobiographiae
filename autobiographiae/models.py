# from email.policy import default
from email.policy import default
from werkzeug.security import generate_password_hash, check_password_hash
from autobiographiae.app import db, loginmanager
from flask_login import UserMixin
from datetime import date

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(1000), nullable=False)
    foto = db.Column(db.String(100), default='foto_usuario.png')
    autobiografia = db.relationship('Autobiografia', backref='usuario', lazy=True, uselist=False, cascade="all, delete")

    def __init__(self, email, nome, senha):
        self.email = email
        self.nome = nome
        self.senha = generate_password_hash(senha)

    def verificar_senha(self, senha):
        return check_password_hash(self.senha, senha)

class Autobiografia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(40000))
    data = db.Column(db.Date, default=date.today())
    autor =  db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False, unique=True)

    def __init__(self, texto, autor):
        self.texto = texto
        self.autor = autor
        

@loginmanager.user_loader
def load_usuarios(id):
    return Usuario.query.get(int(id))