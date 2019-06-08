import os
from flask import Flask, request, jsonify
from . import database
from .util import isnatural, fmt_date


# Global request counter
_request_count = {}

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

def _reset_request_count():
    global _request_count
    _request_count = {}
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
    app.add_url_rule("/difference", view_func=_difference)
    app.before_first_request(_reset_request_count)
    
    # Initialize services
    database.init_app(app)
    
    return app


def _difference():
    try:
        input = request.args["number"]
        if not isnatural(input):
            raise ValueError()
        num = int(input)
        if 0 >= num or num > 100:
            raise ValueError()
    except KeyError:
        return (
            'Missing input - "number" is required and must be a real number 1 - 100',
            400,
            [],
        )
    except ValueError:
        return ('Invalid input - "number" must be a real number 1 - 100', 400, [])

    sqr_sum = 0
    sum = 0
    for i in range(1, num + 1):
        sqr_sum = sqr_sum + (i ** 2)
        sum = sum + i

    diff = (sum ** 2) - sqr_sum

    cnt = _request_count.get(num, 0) + 1
    _request_count[num] = cnt

    return jsonify(
        {
            "datetime": fmt_date(datetime.datetime.now()),
            "value": diff,
            "number": num,
            "occurrences": cnt,
        }
    )
