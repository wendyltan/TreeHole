#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/25 13:51
# @Author  : Wendyltanpcy
# @File    : config.py
# @Software: PyCharm
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = True
    SESSION_COOKIE_NAME = "cookie-tree-hole"
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-is-a-tree-hole'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


