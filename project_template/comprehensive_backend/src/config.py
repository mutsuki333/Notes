# -*- coding: utf-8 -*-
"""
# @file       config.py
# @brief      EventPageGenorator application configuration
"""
import os

# Core modules
from configparser import SafeConfigParser
from configparser import NoSectionError
from configparser import NoOptionError


config = SafeConfigParser()


# Default config file
DEFAULT_PATH = os.getcwd()+'/server.conf'

# The configuration defaults
DEFAULT_CONFIGS = {
    'App': {
        'debug': True,
        'testing': False,
        'secret_key': 'itsasecret',
    },
    'Database': {
        'location': os.getcwd()+'/data/server.db',
    }
}


def load(path=DEFAULT_PATH):
    """
    To load the configuration file
    """
    results = config.read(path)
    if len(results) == 0:
        raise ValueError('Failed to open config file: {0}'.format(path))


def get(section, option):
    """
    To fetch a configuration
    """
    if section not in DEFAULT_CONFIGS:
        raise ValueError('Section: {0} not found'.format(section))

    if option not in DEFAULT_CONFIGS[section]:
        raise ValueError('Option: {0} not found'.format(section))

    try:
        return config.get(section, option)
    except (NoSectionError, NoOptionError):
        return DEFAULT_CONFIGS[section][option]


def getint(section, option):
    """
    To fetch a configuration
    """
    if section not in DEFAULT_CONFIGS:
        raise ValueError('Section: {0} not found'.format(section))

    if option not in DEFAULT_CONFIGS[section]:
        raise ValueError('Option: {0} not found'.format(section))

    try:
        return config.getint(section, option)
    except (NoSectionError, NoOptionError):
        return DEFAULT_CONFIGS[section][option]


def getbool(section, option):
    """
    To fetch a configuration
    """
    if section not in DEFAULT_CONFIGS:
        raise ValueError('Section: {0} not found'.format(section))

    if option not in DEFAULT_CONFIGS[section]:
        raise ValueError('Option: {0} not found'.format(section))

    try:
        return config.getboolean(section, option)
    except (NoSectionError, NoOptionError):
        return DEFAULT_CONFIGS[section][option]


def setup_app(app):
    """
    Setup application configurations
    """
    load()
    app.config['DEBUG'] = getbool('App', 'debug')
    app.config['TESTING'] = getbool('App', 'testing')
    app.config['SECRET_KEY'] = get('App', 'secret_key')
    app.config['DATABASE'] = get('Database', 'location')