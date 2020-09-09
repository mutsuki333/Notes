#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @file       auth/permission.py
# @brief      determin if a user has permission
# @date       2020
# @author     Evan
"""
import functools

from flask_login import current_user

from src import abort
from src.error import ForbiddenRequest

from src.models.Auth import User, Role, UserRoles

def get_roles():
    user_roles = (
        UserRoles
        .select()
        .join(Role)
        .where(UserRoles.user == current_user.id)
    )
    return [ row.role.name for row in user_roles ]

def _has_role(role):
    if current_user.is_anonymous: abort(ForbiddenRequest)
    if not role in get_roles(): abort(ForbiddenRequest)
    return True

def has_role(role):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            _has_role(role)
            return func(*args, **kwargs)
        return wrapper
    return decorator

def is_in_group(group):
    pass

# some shorthands

def root(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        _has_role('root')
        return func(*args, **kwargs)
    return wrapper

def admin(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        _has_role('admin')
        return func(*args, **kwargs)
    return wrapper