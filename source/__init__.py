from flask import Flask, render_template, redirect


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('settings.py')

    @app.route('/sometest')
    def some_test():
        return render_template('basic.html')

    # handling page not found errors
    @app.errorhandler(404)
    def page_not_found(e):
        return 'Page not found', 404

    # handling method not allowed request
    @app.errorhandler(405)
    def method_not_allowed(e):
        return 'Method not allowed', 405

    # registering home blueprints
    from .routes import views
    app.register_blueprint(views.home)

    # registering login, logout and register route
    from .routes import auth
    app.register_blueprint(auth.auth)

    # registering courses page blueprint
    from .routes import courses
    app.register_blueprint(courses.courses)

    from .routes import tutorials
    app.register_blueprint(tutorials.tuts)

    return app
