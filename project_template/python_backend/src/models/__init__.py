#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @file       models/__init__.py
# @brief      register all models to app
# @date       2020
# @author     Evan
"""

from .base import db
from .System import Log
from .Auth import User, Role, UserRoles


model_list = [
    User, Role, UserRoles
]

def setup(location):
    db.init(location)
    db.connect()
    for model in model_list:
        if not model.table_exists():
            db.create_tables([model], safe=True)
    setup_default_data()

def setup_default_data():
    try:
        root = Role(name="root")
        root.save()
        admin = Role(name = "admin")
        admin.save()
        user = User(username = "admin")
        user.update_password("admin")
        admin_user = UserRoles(user=user, role=admin)
        admin_user.save()
        arec = User(username="arec")
        arec.update_password("arec")
        root_user = UserRoles(user=arec, role=root)
        root_user.save()
        root_user = UserRoles(user=arec, role=admin)
        root_user.save()
    except:
        pass