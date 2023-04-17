# -*- coding: utf-8 -*-
"""
Flask 配置文件
"""

class Config(object):
    """
    通用配置
    """
    SECRET_KEY = 'sink_demo'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevelopmentConfig(Config):
    """
    开发环境配置
    """
    TYPE = 'dev'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///party.db"

configs = {
    'default': DevelopmentConfig,
    'dev': DevelopmentConfig,
}