# -*- coding: utf-8 -*-
"""
# @file       __init__.py
# @brief      flask app
"""

import json
import datetime
import uuid

from flask import request
from flask import Flask
from flask_login import LoginManager, current_user
from flask_restful import abort as fr_abort
from peewee import SqliteDatabase

from src.error import WebapiError
from src import config
# from src.models.Log import Log
from src.models import db
from src.models.Auth import User

# Web API verion
version = '0.0.1'

# Application instance
app = Flask(__name__)
config.setup_app(app)

login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id):
    return User.get(User.id == user_id)
login_manager.init_app(app)

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        elif isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, uuid.UUID):
            return obj.hex
        return json.JSONEncoder.default(self, obj)

app.config['RESTFUL_JSON'] = {'cls':CustomEncoder}

from flask_cors import CORS
CORS(app, supports_credentials=True)

@app.before_request
def before_request():
    db.connect(reuse_if_open=True)

@app.after_request
def log_request_after(response):
    """
    function to log each request
    """
    # x_forworded_for = request.headers.get('X-Forwarded-For')
    # if x_forworded_for:
    #     req_from = x_forworded_for.split(",")[0]
    # else: req_from = request.remote_addr
    # req_method = request.method
    # full_path = request.full_path
    # user_id = None if current_user.is_anonymous else current_user.id

    # if 'Content-Type' in request.headers and \
    #     'application/json' in request.headers['Content-Type']:
    #     app.logger.info('{0}: [{1}] {2} data={3}'.
    #         format(req_from, req_method, full_path, request.data))
    # else:
    #     app.logger.info('{0}: [{1}] {2}'.
    #         format(req_from, req_method, full_path))
    # log = Log(
    #     ip=req_from,
    #     path=full_path,
    #     access_type=req_method,
    #     who=user_id,
    #     message=response._status,
    #     data=request.data if request.data else None)
    # log.save()
    db.close()
    return response


def make_response(message='', code=200):
    """
    webapi response
    """
    return {'message': message}, code


def abort(obj, fmt=None):
    """
    webapi abort
    """
    error = obj if issubclass(obj, WebapiError) else WebapiError

    print ('code: {0}'.format(error.code))
    fr_abort(error.status, message=error.message.format(fmt), code=error.code)

