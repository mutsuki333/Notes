#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @file       models/base.py
# @brief      base model
# @date       2020
# @author     Evan
"""

from peewee import Model
from peewee import SqliteDatabase

db = SqliteDatabase(None)

class BaseModel(Model):
    class Meta:
        database = db