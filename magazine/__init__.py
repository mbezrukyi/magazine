from flask import Flask

from .extensions import db, login_manager, migrate
from .models import Article, Topic


def create_app(config_file='settings.py') -> Flask:
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)

    migrate.init_app(app, db)

    login_manager.init_app(app)

    return app
