# from email.policy import default
from email.policy import default
from app import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    foto = db.Column(db.String(100), default='foto_usuario.png')
    autobiografia = db.relationship('Autobiografia', backref='usuario', lazy=True, uselist=False)

    def __init__(self, email, nome, senha):
        self.email = email
        self.nome = nome
        self.senha = senha
        
class Autobiografia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(20000))
    data = db.Column(db.Date)
    fonte = db.Column(db.String(100), default='Apple Chancery, cursive')
    autor =  db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False, unique=True)

    def __init__(self, texto, data, autor):
        self.texto = texto
        self.data = data
        self.autor = autor
        

