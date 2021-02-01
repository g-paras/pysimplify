from flask import Blueprint

home = Blueprint('home', __name__, url_prefix='/home')


@home.route('/')
def index():
    return 'You are on index home route'
