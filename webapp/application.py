import functools

from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from webapp.database import db_session
from webapp.database import User

bp = Blueprint('application', __name__, url_prefix='/')

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

# This is the endpoint for the "Search for Ratings" page.
@bp.route("/search_for_ratings", methods=["GET", "POST"])
def search_for_ratings():
    if request.method == "POST":
        student_organization_name = request.form.get("student_organization_name")

        #if not student_organization_name:
            #return apology("must enter name of student organization")

        student_organization_id = db_session.execute("SELECT id FROM student_organizations WHERE name =:student_organization_name", {'student_organization_name':student_organization_name})
        
        # Return error if no match.
        #if not stock:
            #return apology("no stock matches symbol")
        
        student_organization_ratings = db_session.execute("SELECT racial_identity_inclusivity, ethnic_identity_inclusivity, gender_identity_inclusivity, sexual_orientation_inclusivity, socioeconomic_status_inclusivity, religious_identity_inclusivity, disability_identity_inclusivity FROM ratings WHERE student_organization_id =:student_organization_id", {'student_organization_id':student_organization_id})

        return render_template("ratings.html", student_organization_ratings=student_organization_ratings, student_organization_name=student_organization_name)

    else:
        return render_template("search_for_ratings.html")
