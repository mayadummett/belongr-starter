import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from webapp.database import db_session
from webapp.database import User, Student_Organization, Rating

bp = Blueprint('application', __name__, url_prefix='/')

# This is the endpoint for the "Index" page.
@bp.route("/index", methods=["GET", "POST"])
def index():
    return render_template("index.html")

# This is the endpoint for the "Sign In" page.
@bp.route("/sign-in", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            flash("Password and username required.")
            return redirect("/login")

        return render_template("index.html")
    else:
        return render_template("sign_in.html")

# This is the endpoint for the "Sign Up" page.
@bp.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    return render_template("sign_up.html")

# This is the endpoint for the "Change Password" page.
@bp.route("/change-password", methods=["GET", "POST"])
def change_password():
    return render_template("change_password.html")

# This is the endpoint for the "Search for Ratings" page.
@bp.route("/search-for-ratings", methods=["GET", "POST"])
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

# This is the endpoint for the "Your Ratings" page.
@bp.route("/your-ratings", methods=["GET", "POST"])
def your_ratings():
    return render_template("your_ratings.html")
