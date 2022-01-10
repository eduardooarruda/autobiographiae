from flask import Blueprint, render_template

bp = Blueprint('autenticacao', __name__, url_prefix="/autenticacao" ,template_folder="templates")

@bp.route("/login")
def login():
    return render_template("login.html")
