from flask import Blueprint, render_template
from flask_login import login_required
bp = Blueprint('QRcode',__name__, url_prefix="/QRcode", template_folder="templates", static_folder="static", static_url_path='/static')

@bp.route("/", methods=['GET', 'POST'])
@login_required
def qrcode():
    return render_template("qrcode.html")