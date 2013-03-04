from flask import Blueprint, render_template, session, redirect, url_for, \
    request, flash, g, jsonify, abort

mod = Blueprint('general', __name__, url_prefix='/')

@mod.route('/')
def hello_world():
    return render_template("index.html")

