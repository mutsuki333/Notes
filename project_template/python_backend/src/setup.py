#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @file       setup.py
# @brief      flask app setup
# @date       2020
# @author     Evan
"""

from src import app

from src.logger import setup as logger_setup
from src import config
from src.resource import setup as api_setup
from src.models import setup as db_setup

logger_setup()
api_setup(app)
db_setup(app.config['DATABASE'])
