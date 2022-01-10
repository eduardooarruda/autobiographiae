from flask import Flask, render_template


def create_app():

    app = Flask(__name__)

    with app.app_context():
        
        from home import home
        app.register_blueprint(home.bp)

        from autenticacao import autenticacao
        app.register_blueprint(autenticacao.bp)

    return app
