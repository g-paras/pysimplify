from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('settings.py')

    @app.route('/')
    def home():
        return 'Welcome to pysimplify'

    from . import views
    app.register_blueprint(views.home)

    return app
