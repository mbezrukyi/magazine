from flask import Flask

from .extensions import db, login_manager


def create_app(config_file='settings.py') -> Flask:
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)

    login_manager.init_app(app)

    return app
