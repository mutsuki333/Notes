#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @file       resource/__init__.py
# @brief      register all resource to app
# @date       2020
# @author     Evan
"""

# Web framework
from flask_restful import Api

from src import app
from src import config

from .test import TestLogin, TestLogout, TestRole

# RESTful API instance
api = Api(app, catch_all_404s=True)


def setup(app):
    # base = config.get('App','base_url')

    # api.add_resource(
    #     PageSearch,
    #     base+'/pagesearch'
    # )









    api.add_resource(TestLogin,'/test/login')
    api.add_resource(TestLogout,'/test/logout')
    api.add_resource(TestRole,'/test/role')