from flask import Blueprint, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField
from wtforms.validators import DataRequired

bp = Blueprint('autenticacao', __name__,
               url_prefix="/autenticacao", template_folder="templates", static_folder="static", static_url_path='/static')

#Formulario

class CadastroForm(FlaskForm):
    foto = FileField(label='Foto:', name='foto')
    nome = StringField(label='Nome:', name='nome', validators=[DataRequired()], id="nome")
    email = StringField(label='Email:', name='email', validators=[DataRequired()], id="email")
    senha = PasswordField(label='Senha', name='senha', validators=[DataRequired()], id="senha")

@bp.route("/login")
def login():
    return render_template("login.html")


@bp.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    form = CadastroForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            nome = request.form['nome']
            email = request.form['email']
            senha = request.form['senha']
            return f"Nome: {nome}, Senha: {senha}, email: {email}"

    return render_template("cadastrar.html", form=form)
