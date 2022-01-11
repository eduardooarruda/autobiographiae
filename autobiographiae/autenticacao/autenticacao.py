from flask import Blueprint, render_template

bp = Blueprint('autenticacao', __name__,
               url_prefix="/autenticacao", template_folder="templates", static_folder="static", static_url_path='/static')


@bp.route("/login")
def login():
    return render_template("login.html")


@bp.route('/cadastrar')
def cadastrar():
    return render_template("cadastrar.html")
