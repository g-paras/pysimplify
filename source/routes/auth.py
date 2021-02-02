from flask import Blueprint, render_template

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/login')
def users():
    return render_template('login.html')
