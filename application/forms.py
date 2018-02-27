#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/25 22:38
# @Author  : Wendyltanpcy
# @File    : forms.py
# @Software: PyCharm
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, ValidationError, Email, EqualTo

from application.models import User


class TalkForm(FlaskForm):
    talk = TextAreaField('Say something you want to throw in the hole',
                         validators=[DataRequired(),Length(min=1,max=140)])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    password2 = PasswordField('Repeat Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username')

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address')