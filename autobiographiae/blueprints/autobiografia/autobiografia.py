from flask import Blueprint, render_template, request, Response
from flask_login import login_required, current_user
from autobiographiae.models import Autobiografia, Usuario
from autobiographiae.app import db

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

@bp.post("/pesquisar-autobiografia")
def pesquisar_autobiografia():
    nome_usuario = request.form['nome_usuario']
    pesquisa = f"%{nome_usuario}%"
    lista_usuarios = Usuario.query.filter(Usuario.nome.like(pesquisa)).all() 
    qtd_usuarios = len(lista_usuarios)
    
    if qtd_usuarios:
        resultado = f"Resultado: {qtd_usuarios}" 
        return render_template("lista_usuarios.html", lista_usuarios=lista_usuarios, resultado=resultado)
    else:
        resultado = "Nenhum resultado foi encontrado"
        return render_template("lista_usuarios.html", resultado=resultado)

@bp.get("/mostrar-autobiografia/<id_usuario>")
def mostrar_autobiografia(id_usuario):
    usuario = Usuario.query.filter_by(id=id_usuario).first()
    return render_template("autobiografia.html", usuario=usuario)
