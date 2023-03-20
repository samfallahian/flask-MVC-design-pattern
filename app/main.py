from flask import Flask
from config import Config
from app.models import schema


def create_app():
    app = Flask(__name__, template_folder=Config.TEMPLATE_PATH)
    app.secret_key = Config.SECRET_KEY
    app.debug = True

    # Initialize Database
    schema.index()

    # Register blueprints here
    from app.controllers import bp_main, bp_resources
    app.register_blueprint(bp_main)
    app.register_blueprint(bp_resources, url_prefix='/resources')

    return app


APP = create_app()

if __name__ == '__main__':
    APP.run(debug=True)
