from flask import Flask

from app.core import core
from app.blog import blog


def create_app(config=None):

    app = Flask(__name__)

    if config is not None:
        app.config.from_pyfile(config)

    app.register_blueprint(core)
    app.register_blueprint(blog)

    return app
