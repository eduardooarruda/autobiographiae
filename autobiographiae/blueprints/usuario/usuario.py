from flask import Blueprint

bp = Blueprint('usuario', __name__,
               url_prefix="/usuario", template_folder="templates", static_folder="static")

@bp.route("/perfil", methods=['GET', 'POST'])
def autobiografia():
    return "<h1>Perfil</h1>"
