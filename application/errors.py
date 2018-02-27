#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 10:33
# @Author  : Wendyltanpcy
# @File    : errors.py
# @Software: PyCharm
from flask import render_template
from flask_wtf.csrf import CSRFError

from application import app, db


@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('csrf_error.html',reason=e.description),400

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'),500