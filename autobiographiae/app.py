from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def create_app():

    app = Flask(__name__)

    if app.config["ENV"] == 'production':
        app.config.from_object('config.ProductionConfig')
    elif app.config["ENV"] == 'development':
        app.config.from_object('config.DevelopmentConfig')

    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)

    with app.app_context():

        from autobiographiae.blueprints.home import home
        app.register_blueprint(home.bp)

        from autobiographiae.blueprints.autenticacao import autenticacao
        app.register_blueprint(autenticacao.bp)

        from autobiographiae.blueprints.QRcode import QRcode
        app.register_blueprint(QRcode.bp)

        from autobiographiae.error_routes import page_not_found
        app.register_error_handler(404, page_not_found)

    return app
