# from email.policy import default
from email.policy import default
from werkzeug.security import generate_password_hash, check_password_hash
from autobiographiae.app import db, loginmanager
from flask_login import UserMixin
from datetime import date
from markdown import markdown

def verificar_tagHTML(texto):
    tags_html = ['<form', '<a','<input']
    for tag in tags_html:
        if tag in texto:
            return '<h2 style="color: red; background: Gold; border: 1px solid; padding: 10px;">No seu texto foi encontrado tags HTML, por favor redija seu texto novamente sem adicionar tags HTML.<h2>'
    return markdown(texto, extensions=['tables','def_list', 'admonition', 'meta','fenced_code'])

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
        self.texto = verificar_tagHTML(texto)
        self.autor = autor
        

@loginmanager.user_loader
def load_usuarios(id):
    return Usuario.query.get(int(id))