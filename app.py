from flask import Flask, render_template


def create_app():

    app = Flask(__name__)

    with app.app_context():

        @app.route("/")
        @app.route("/home")
        def hello_world():
            return render_template("index.html")
        
        @app.route("/login")
        def login():
            return render_template("login.html")
            
    return app
