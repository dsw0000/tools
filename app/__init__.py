# -*- coding: utf-8 -*-
from __future__ import absolute_import

import logging.config
import os

from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from itsdangerous import TimedJSONWebSignatureSerializer

# from app.errors import AuthFailure


app_path = os.path.abspath(os.path.dirname(__file__))
static_path = os.path.join(app_path, "static")


def create_app():
    # logging.config.fileConfig(os.path.join(os.path.abspath(os.path.dirname(__file__)), "logging.conf"))
    app = Flask(__name__, static_folder='./static')
    # UPLOAD_FOLDER = os.path.join(app_path, "uploads")
    # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    Limiter(key_func=get_remote_address, headers_enabled=True, default_limits=["1000/minute"]).init_app(app)
    from app.weather_v1 import bp
    app.register_blueprint(
        bp,
        url_prefix='/weather/v1'
    )
    return app

