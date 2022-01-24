from flask import Blueprint, render_template

bp = Blueprint('autobiografia', __name__,
               url_prefix="/autobiografia", template_folder="templates", static_folder="static")

@bp.get("/")
def autobiografia():
    return render_template('autobiografia.html')


@bp.route("/adicionar", methods=['GET', 'POST'] )
def adicionar():
    return render_template('addAutobiografia.html')
