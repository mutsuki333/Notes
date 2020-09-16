#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @file       models/Auth.py
# @brief      Models related to User authorization
# @date       2020
# @author     Evan
"""


import hmac
import uuid
import datetime
import binascii
import random
import string
from base64 import b64decode

from peewee import CharField
from peewee import TextField
from peewee import IntegerField
from peewee import BooleanField
from peewee import DateTimeField
from peewee import PrimaryKeyField
from peewee import ForeignKeyField
from flask_login import UserMixin
from passlib.utils.pbkdf2 import pbkdf2

from .base import BaseModel


class User(BaseModel, UserMixin):
    id = PrimaryKeyField(db_column='id')
    username = CharField(unique=True)
    password_hash = CharField()
    password_salt = CharField(null=True)
    modified_at = DateTimeField(default=datetime.datetime.utcnow())
    created_at = DateTimeField(default=datetime.datetime.utcnow())

    def save(self, *args, **kwargs):
        """
        Override save function to auto updata modified_at.
        """
        self.modified_at = datetime.datetime.utcnow()
        return super(User, self).save(*args, **kwargs)

    def verify_password(self, username, password):
        """
        Verify whether password is valid.
        @param username (string):
            User name string.
        @param password (string):
            Password string.

        @return (boolen):
            Whether is the valid password.
        """
        check_data = ''

        if self.password_salt:
            check_data = hash_encode(password, self.password_salt)
        else:
            check_data = hash_encode(password, username)

        if self.password_hash == check_data:
            return True
        else:
            return False

    def update_password(self, new_password):
        """
        Function to update the password
        """
        if not new_password:
            return False

        if not self.password_salt:
            self.password_salt = uuid.uuid4().hex

        self.password_hash = hash_encode(new_password, self.password_salt)
        self.save()

        return True
    
    def get_obj(self):
        obj = {}
        obj["username"] = self.username

        return obj


class Role(BaseModel):
    id = PrimaryKeyField(db_column='id')
    name = CharField(unique=True)
    description = TextField(null=True)
    modified_at = DateTimeField(default=datetime.datetime.utcnow())
    created_at = DateTimeField(default=datetime.datetime.utcnow())

    def save(self, *args, **kwargs):
        self.modified_at = datetime.datetime.utcnow()
        return super(Role, self).save(*args, **kwargs)

class UserRoles(BaseModel):
    id = PrimaryKeyField(db_column='id')
    user = ForeignKeyField(User, backref='UserRoles')
    role = ForeignKeyField(Role, backref='UserRoles')

def hash_encode(password, salt, iterations=None):
    """
    Perform password encoding and generate credential
    @param password (string):
        Raw password string
    @param salt (string):
        Salt value for generating credential
    @param iterations (integer):
        Number of iterations of hash process

    @return credential (string):
        Encoded credential
    """
    assert password
    assert salt and '$' not in salt
    if type(password) is str:
        password = password.encode()
    if type(salt) is str:
        salt = salt.encode()
    if iterations is None:
        iterations = 1000
    credential = pbkdf2(password, salt, iterations)
    credential = binascii.b2a_hex(credential)
    credential = credential.decode()

    return credential

def random_code(length=5):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str