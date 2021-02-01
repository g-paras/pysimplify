from flask import Blueprint, render_template

user = Blueprint('user', __name__, url_prefix='/login')


@user.route('/')
def users():
    return render_template('login.html')
