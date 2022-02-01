from flask import Blueprint, render_template

bp = Blueprint('usuario', __name__,
               url_prefix="/usuario", template_folder="templates", static_folder="static")

@bp.route("/perfil", methods=['GET', 'POST'])
def perfil():
    return render_template("perfil.html")
