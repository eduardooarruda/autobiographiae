from email.policy import default
from werkzeug.security import generate_password_hash, check_password_hash
from autobiographiae.app import db, loginmanager
from flask_login import UserMixin
from datetime import date

def verificar_tagHTML(texto):
    tags_html = [
        '<!- -', '<!DOCTYPE', '<a', '<abbr', '<address', '<area', '<article',
        '<aside', '<audio', '<b', '<base', '<bdo', '<blockquote', '<body',
        '<br','<button', '<canvas', '<caption', '<cite', '<code', '<col',
        '<colgroup', '<command', '<datalist', '<dd', '<de', '<details', '<div', '<dl', '<dt', '<em', '<embed', '<fieldset', '<figcaption', '<figure', '<footer', '<form', '<h1', '<h2', '<h3', '<h4', '<h5', 'h6','<head', '<header', '<hgroup', '<hr', '<html', '<i', '<iframe',
        '<img', '<input', '<ins', '<kbd', '<labe', '<legend', '<li', '<link', '<map', '<mark', '<menu', '<meta', '<meter', '<nav', '<noscript', '<object', '<ol', '<optgroup', '<option', '<output',
        '<p', '<param', '<pre', '<progress', '<q', '<ruby', '<rp', '<rt',
        '<samp', '<script', '<section', '<select', '<small', '<source', 
        '<span', '<strong', '<style', '<sub', '<sup', '<tbody', '<td',
        '<textarea', '<tfoot', '<th', '<thead', '<time', '<title', '<tr',
        '<ul', '<var', '<video'
        ]
        
    for tag in tags_html:
        if tag in texto:
            return '<h2 style="color: red; background: Gold; border: 1px solid; padding: 10px;">No seu texto foi encontrado tags HTML, por favor redija seu texto novamente sem adicionar tags HTML.<h2>'
    return texto

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