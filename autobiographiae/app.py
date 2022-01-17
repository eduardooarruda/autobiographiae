from flask import Flask, render_template
import os
SECRET_KEY = os.urandom(32)

def create_app():

    app = Flask(__name__)

    with app.app_context():
        app.config['SECRET_KEY'] = SECRET_KEY
        
        from home import home
        app.register_blueprint(home.bp)

        from autenticacao import autenticacao
        app.register_blueprint(autenticacao.bp)

        from error_routes import page_not_found
        app.register_error_handler(404, page_not_found)
        

    return app
