from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
loginmanager = LoginManager()

def create_app():

    app = Flask(__name__)

    if app.config["ENV"] == 'production':
        app.config.from_object('config.ProductionConfig')
    elif app.config["ENV"] == 'development':
        app.config.from_object('config.DevelopmentConfig')

    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    loginmanager.init_app(app)

    with app.app_context():
        loginmanager.login_view = '/autenticacao/login'
        loginmanager.login_message = "Faça login para acessar a página!"
        from autobiographiae.blueprints.home import home
        app.register_blueprint(home.bp)

        from autobiographiae.blueprints.autenticacao import autenticacao
        app.register_blueprint(autenticacao.bp)

        from autobiographiae.blueprints.QRcode import QRcode
        app.register_blueprint(QRcode.bp)

        from autobiographiae.blueprints.usuario import usuario
        app.register_blueprint(usuario.bp)

        from autobiographiae.blueprints.autobiografia import autobiografia
        app.register_blueprint(autobiografia.bp)
        
        from autobiographiae.error_routes import page_not_found
        app.register_error_handler(404, page_not_found)

    return app
