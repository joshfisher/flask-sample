import os
from flask import Flask
from . import database, difference


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    # Configuration
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, "app.sqlite"),
    )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # Make sure instance dir exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Configure routes
    app.add_url_rule("/difference", view_func=difference.handler)
    
    # Initialize services
    database.init_app(app)
    
    return app
