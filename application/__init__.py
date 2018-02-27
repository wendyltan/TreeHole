#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/25 13:45
# @Author  : Wendyltanpcy
# @File    : __init__.py
# @Software: PyCharm
from flask import Flask
from flask_login import LoginManager

from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app,db)

login = LoginManager(app)
login.login_view = 'login'


from application import routes,models,errors