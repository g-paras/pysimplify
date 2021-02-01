from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('settings.py')

    @app.route('/')
    def home():
        return render_template('index.html')

    from .views import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .login import user as user_blueprint
    app.register_blueprint(user_blueprint)

    from .routes import skile
    app.register_blueprint(skile.skt)

    return app
