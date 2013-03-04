from flask import Blueprint, render_template, session, redirect, url_for, \
    request, flash, g, jsonify, abort
from flaskskeleton.database import Users
from flaskskeleton.forms import LoginForm
from flaskskeleton import login_manager
from flask.ext.login import (LoginManager, current_user, login_required,
                            login_user, logout_user, UserMixin, AnonymousUser,
                            confirm_login, fresh_login_required)
mod = Blueprint('usermgmt', __name__)

class User(UserMixin):
    def __init__(self, name, id, active=True):
        self.name = name
        self.id = id
        self.active = active
    
    def is_active(self):
        return self.active

@mod.route('/')
def hello_world():
    return render_template("index.html")

@mod.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template("login.html", form=LoginForm())
    if request.method == "POST":
        form = LoginForm(request.form)
        if form.validate():
            dbuser = Users.get_by_name_pw(form.username.data, form.password.data)
            user = None
            if dbuser:
                user = User(dbuser['email'], dbuser['token'])

            if user and login_user(user, remember=True):
                flash("Logged in!")
                return render_template("index.html", form=form)
            else:
                return render_template("login.html", form=form)
        else:
            return render_template("login.html", form=form)
    return render_template("login.html")

@mod.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(somewhere)

@login_manager.user_loader
def load_user(id):
    return Users.get_by_token(id)
