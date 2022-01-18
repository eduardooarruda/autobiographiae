from email.policy import default
from app import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    foto = db.Column(db.String(100), default='foto_usuario.png')

    def __init__(self, email, nome, senha):
        self.email = email
        self.nome = nome
        self.senha = senha
        
