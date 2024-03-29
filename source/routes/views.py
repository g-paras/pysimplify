from flask import Blueprint, render_template

home = Blueprint('home', __name__)


@home.route('/')
def index():
    return render_template('index.html')


@home.route('/about')
def about():
    return render_template('about.html')


@home.route('/quizes')
def quizes():
    return render_template('quiz.html')
