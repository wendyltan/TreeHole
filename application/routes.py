#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/25 13:48
# @Author  : Wendyltanpcy
# @File    : routes.py
# @Software: PyCharm
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.urls import url_parse

from application import app, db
from application.forms import TalkForm, LoginForm, RegistrationForm
from application.models import Talk, User


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    title = 'Tree Hole'
    form = TalkForm()
    cur_status = False
    if form.validate_on_submit():
        talk= Talk(body=form.talk.data,user_id=current_user.id)
        db.session.add(talk)
        db.session.commit()
        flash('Your talk has been thrown into the hole!')
        return redirect(url_for('index'))

    '''
    deal with DELETE operation
    must distinguish with the normal form post
    to avoid accident
    
    '''
    if request.method=="POST" and request.form['submit']=="delete":
        talk_id = request.form['hidden']
        talk = Talk.query.filter_by(id=talk_id).first()
        db.session.delete(talk)
        db.session.commit()
        flash('Your talk has been deleted!')
        return redirect(url_for('index'))

    talks = Talk.query.all()
    if not talks:
        global cur_status
        cur_status = True

    return render_template('index.html',cur_status=cur_status,title=title, talks=talks, form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    #else haven't login, ask for login
    form = LoginForm()
    if form.validate_on_submit():
        #find the user
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            #no such password or wrong password
            flash('Invalid username or password!')
            return redirect(url_for('login'))
        #else ,login success
        login_user(user,remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html',title='Sign in',form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
