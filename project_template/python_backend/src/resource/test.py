#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @file       resource/test.py
# @brief      this is for test usage
# @date       2020
# @author     Evan
"""

import datetime

from flask_restful import Resource
from flask_restful import reqparse

from flask_login import login_required, login_user, logout_user, current_user
from playhouse.shortcuts import model_to_dict, update_model_from_dict

from src import abort, make_response
from src.error import Notfound
from src import permission

from src.models.Auth import User

import logging
log = logging.getLogger(__name__)

class TestLogin(Resource):
    def get(self):
        user = User.get(User.username == "admin")
        login_user(user, remember=True)
        log.info("login")
        return make_response("ok")

class TestLogout(Resource):
    def get(self):
        logout_user()
        return make_response("ok")

class TestRole(Resource):
    @permission.require_role('admin')
    def get(self):
        print()
        return make_response("ok")
    
    @permission.root
    def post(self):
        return {'Role': "root"}