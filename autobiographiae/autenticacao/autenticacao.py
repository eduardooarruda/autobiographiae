from flask import Blueprint, render_template, request
from .forms.formCadastro import CadastroForm
from .forms.formLogin import LoginForm

bp = Blueprint('autenticacao', __name__,
               url_prefix="/autenticacao", template_folder="templates", static_folder="static", static_url_path='/static')

@bp.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            email = form.email.data
            # email = request.form['email']
            senha = form.senha.data
            # senha = request.form['senha']
            return f"Email: {email}, Senha: {senha}"

    return render_template("login.html", form=form)


@bp.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    form = CadastroForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            nome = request.form['nome']
            email = request.form['email']
            senha = request.form['senha']
            return f"Nome: {nome}, Senha: {senha}, email: {email}"
        # else:
        #     return 'O formulário não foi falidado'
    return render_template("cadastrar.html", form=form)
