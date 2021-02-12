from flask import Blueprint, render_template

tuts = Blueprint('tuts', __name__, url_prefix='/tutorials')


@tuts.route('/')
def main():
    return render_template('tutorials.html')
