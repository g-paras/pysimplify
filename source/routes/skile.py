from flask import Blueprint

skt = Blueprint('skt', __name__, url_prefix='/skt')


@skt.route('/')
def func():
    return 'A route from another directory'
