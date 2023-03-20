from flask import Blueprint

bp_main = Blueprint('main', __name__)
bp_resources = Blueprint('resources', __name__)

from app.controllers import main, resources
