from flask import Blueprint, render_template, request, Response
from flask_login import login_required, current_user
from autobiographiae.models import Autobiografia, Usuario
from autobiographiae.app import db
import datetime

bp = Blueprint('autobiografia', __name__,
               url_prefix="/autobiografia", template_folder="templates", static_folder="static")

@bp.get("/")
def autobiografia():
    return render_template('autobiografia.html')


@bp.route("/adicionar", methods=['GET', 'POST'] )
@login_required
def adicionar():
    if request.method == 'POST':
        texto = request.form['texto']
        autobiografia = Autobiografia(texto, current_user.id)
        db.session.add(autobiografia)
        db.session.commit()
        
    return render_template('addAutobiografia.html')
