from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# import os
# SECRET_KEY = os.urandom(32)

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)

    if app.config["ENV"] == 'production':
        app.config.from_object('config.ProductionConfig')
    elif app.config["ENV"] == 'development':
        app.config.from_object('config.DevelopmentConfig')
    
    db.init_app(app)
    
    with app.app_context():
        # app.config['SECRET_KEY'] = SECRET_KEY
        
        from home import home
        app.register_blueprint(home.bp)

        from autenticacao import autenticacao
        app.register_blueprint(autenticacao.bp)

        from error_routes import page_not_found
        app.register_error_handler(404, page_not_found)
        # print(f'senha = {app.config["SECRET_KEY"]}')

    return app
