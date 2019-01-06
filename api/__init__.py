from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api.config import Config

# create db connection
db = SQLAlchemy()


def create_app(config_class=Config):
    """Create instance of app with given config
    Args:
        Param1(object) : config_class - object of config file

    Returns:
        Param1(object) : instance of app

    """

    app = Flask(__name__)
    app.config.from_object(Config)

    db.app = app
    db.init_app(app)

    # register Blueprint for route connection
    from api.utils.routes import utils

    app.register_blueprint(utils)

    return app
