import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from webapp.database import db_session
from webapp.database import User

bp = Blueprint('group1', __name__, url_prefix='/')

#Endpoint for the Home Page
@bp.route("/index", methods=["GET", "POST"])
def index():
    """Default endpoint for the system"""
    return render_template("index.html")

#Endpoint for Login
@bp.route("/sign_in", methods=["GET", "POST"])
def login():
    """Default endpoint for the system"""
    return render_template("sign_in.html")

#Endpoint for Register
@bp.route("/sign_up", methods=["GET", "POST"])
def register():
    """Default endpoint for the system"""
    return render_template("sign_up.html")
    