from flask import Blueprint, render_template, request, Response
from flask_login import login_required, current_user
from datetime import date
from markdown import markdown
from autobiographiae.models import Autobiografia, Usuario
from autobiographiae.app import db
from autobiographiae.models import verificar_tagHTML

bp = Blueprint('autobiografia', __name__,
               url_prefix="/autobiografia", template_folder="templates", static_folder="static")


@bp.get("/")
def autobiografia():
    return render_template('autobiografia.html')


@bp.route("/adicionar-autobiografia", methods=['GET', 'POST'] )
@login_required
def adicionar_autobiografia():
    if request.method == 'POST':
        texto = request.form['texto']
        autobiografia = Autobiografia(texto, current_user.id)
        db.session.add(autobiografia)
        db.session.commit()
        
    return render_template('adicionar_editar_Autobiografia.html')

@bp.route("/editar-autobiografia", methods=['GET', 'POST'])
@login_required
def editar_autobiografia():
    if request.method == 'POST':
        id_usuario = current_user.id
        texto = request.form['texto']
        autobiografia =  Autobiografia.query.filter_by(autor=id_usuario).first()
        autobiografia.texto = verificar_tagHTML(texto)
        autobiografia.data = date.today()
        db.session.commit()

    return render_template('adicionar_editar_Autobiografia.html')

@bp.post("/pesquisar-autobiografia")
def pesquisar_autobiografia():
    nome_usuario = request.form['nome_usuario']
    pesquisa = f"%{nome_usuario}%"
    lista_usuarios = Usuario.query.filter(Usuario.nome.like(pesquisa)).all() 
    qtd_usuarios = len(lista_usuarios)
    
    if qtd_usuarios:
        resultado = f"Resultado: " 
        return render_template("lista_usuarios.html", lista_usuarios=lista_usuarios, resultado=resultado)
    else:
        resultado = "Nenhum resultado foi encontrado"
        return render_template("lista_usuarios.html", resultado=resultado)

@bp.get("/mostrar-autobiografia/<id_usuario>")
def mostrar_autobiografia(id_usuario):
    autobiografia = Autobiografia.query.filter_by(autor=id_usuario).first()
    autobiografia_texto = markdown(autobiografia.texto, extensions=['tables','def_list', 'admonition', 'meta','fenced_code'])
    return render_template("autobiografia.html", autobiografia=autobiografia, autobiografia_texto=autobiografia_texto)

@bp.get("/mostrar-todas-autobiografias")
def mostrar_todas_autobiografias():
    resultado = "Todas as autobiografias:"
    todos_usuarios = Usuario.query.order_by(Usuario.nome).all() 
    return render_template("lista_usuarios.html",lista_usuarios=todos_usuarios, resultado=resultado )
