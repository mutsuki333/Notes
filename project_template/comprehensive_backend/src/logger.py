#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @file       logger.py
# @brief      webapi logger setup
# @date       2020
# @author     Evan
"""

# Logging
import logging
import sys

def setup():
    FORMAT = '[%(asctime)s][%(levelname)s][%(filename)s:%(funcName)s():%(lineno)d] %(message)s'
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=FORMAT)