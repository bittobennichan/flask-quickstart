from flask import Flask
from config import config
# config module is available here
# https://github.com/miguelgrinberg/flasky/issues/154
# By default, the current directory for a process is the directory
# from where the application was started.

# Load all your extensions below ...
# Eg.
# from flask_sqlalchemy import SQLAlchemy
# from flask_bootstrap import Bootstrap
# db = SQLAlchemy()
# bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Configure the extensions below ...
    # Eg.
    # db.init_app(app)
    # bootstrap.init_app(app)

    # This is the main Blueprint
    from .main.views import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # Register other Blueprints below ...

    return app
