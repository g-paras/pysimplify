from flask import Blueprint, render_template

courses = Blueprint('courses', __name__, url_prefix='/courses')


@courses.route('/')
def list_courses():
    return render_template('courses.html')
