from flask import render_template
from app.controllers import bp_main


@bp_main.route('/')
def index():
    return render_template('home.html')
