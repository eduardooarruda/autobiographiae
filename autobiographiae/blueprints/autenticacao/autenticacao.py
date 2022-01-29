from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, login_user, logout_user
from .forms.formCadastro import CadastroForm
from .forms.formLogin import LoginForm
from autobiographiae.models import Usuario

# from autobiographiae.models import Autobiografia
from autobiographiae.app import db


bp = Blueprint('autenticacao', __name__,
               url_prefix="/autenticacao", template_folder="templates", static_folder="static")


@bp.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            email = form.email.data
            usuario = Usuario.query.filter_by(email=email).first()

            if usuario and usuario.verificar_senha(form.senha.data):
                login_user(usuario)
                flash(f"Seja bem vindo {usuario.nome}!")
                return redirect(url_for('home.home'))
            else:
                flash('E-mail ou senha invalida!')
                return redirect(url_for('autenticacao.login'))

    return render_template("login.html", form=form)


@bp.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    form = CadastroForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            nome = request.form['nome']
            email = request.form['email']
            senha = request.form['senha']
            if Usuario.query.filter_by(email=email).first():
                flash("Este e-mail já foi cadastrado!")
                return redirect(url_for('autenticacao.cadastrar'))
            else:
                novo_usuario = Usuario(email, nome, senha)
                db.session.add(novo_usuario)
                db.session.commit()
                flash(f'Seja bem vindo, {nome}')
                return redirect(url_for('home.home'))

    return render_template("cadastrar.html", form=form)


@bp.get('/logout')
@login_required
def logout():
    logout_user()
    flash('Você não está mais logado!')
    return redirect('/')