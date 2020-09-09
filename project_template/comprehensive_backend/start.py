#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @file       start.py
# @brief      the start file for uwsgi to start
# @date       2020
# @author     Evan
"""

import os
from src.setup import app

if __name__ == '__main__':
    app.run()
