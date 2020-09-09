#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @file       models/System.py
# @brief      Models related to System
# @date       2020
# @author     Evan
"""

import datetime

from peewee import CharField
from peewee import TextField
from peewee import IntegerField
from peewee import BooleanField
from peewee import DateTimeField
from peewee import PrimaryKeyField
from peewee import ForeignKeyField

from .base import BaseModel

class Log(BaseModel):
    id = PrimaryKeyField(db_column='id')
    name = CharField(unique=True)
    description = TextField(null=True)
    modified_at = DateTimeField(default=datetime.datetime.utcnow())
    created_at = DateTimeField(default=datetime.datetime.utcnow())

    def save(self, *args, **kwargs):
        self.modified_at = datetime.datetime.utcnow()
        return super(Role, self).save(*args, **kwargs)