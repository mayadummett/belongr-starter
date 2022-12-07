from flask import Blueprint, flash, redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash
from webapp.database import db_session
from webapp.database import User, Rating
from functools import wraps
from numpy import median, mean
import matplotlib.pyplot as plt

bp = Blueprint('application', __name__, url_prefix='/')

# This is the endpoint for the "Index" page.
@bp.route("/index", methods=["GET", "POST"])
def index():
    return render_template("index.html")

# This is the endpoint for the "Sign In" page.
@bp.route("/sign-in", methods=["GET", "POST"])
def sign_in():
    session.clear()
    
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            flash("All fields must be completed.")
            return redirect("/sign-in")

        rows = db_session.execute("SELECT id, password FROM users WHERE email =:email", {'email':email}).first()

        if not rows or not check_password_hash(rows["password"], password):
            flash("Email and/or password is incorrect.")
            return redirect("/sign-in")

        session["user_id"] = rows["id"]

        return redirect("/")
    else:
        return render_template("sign_in.html")

# This decorates routes to require successful completion of the "Sign In" page.
def sign_in_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/sign-in")
        return f(*args, **kwargs)
    return decorated_function

# This is the endpoint for the "Sign Out" page.
@bp.route("/sign-out")
@sign_in_required
def sign_out():
    session.clear()
    return redirect("/sign-in")

# This is the endpoint for the "Sign Up" page.
@bp.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        password_initial = request.form.get("password_initial")
        password_confirmation = request.form.get("password_confirmation")

        if not (email and password_initial and password_confirmation):
            flash("All fields must be completed.")
            return redirect("/sign-up")

        if password_initial != password_confirmation:
            flash("Passwords do not match.")
            return redirect("/sign-up")
        
        rows = db_session.execute("SELECT id FROM users WHERE email =:email",{'email':email}).first()
        if rows:
            flash("Email is already taken.")
            return redirect("/sign-up")
        
        user = User(email=email, password=generate_password_hash(password_initial))
        db_session.add(user)
        db_session.commit()

        flash("Success!")

        return redirect("/sign-in")
    else:
        return render_template("sign_up.html")

# This is the endpoint for the "Change Password" page.
@bp.route("/change-password", methods=["GET", "POST"])
@sign_in_required
def change_password():
    if request.method == "POST":

        email = request.form.get("email")
        old_password = request.form.get("old_password")
        new_password_initial = request.form.get("new_password_initial")
        new_password_confirmation = request.form.get("new_password_confirmation")
    
        if not (email and old_password and new_password_initial and new_password_confirmation):
            flash("All fields must be completed.")
            return redirect("/change-password")

        if new_password_initial != new_password_confirmation:
            flash("New passwords do not match.")
            return redirect("/change-password")
        
        rows = db_session.execute("SELECT password FROM users WHERE email =:email", {'email':email}).first()

        if not rows or not check_password_hash(rows["password"], old_password):
            flash("Email and/or old password is incorrect.")
            return redirect("/change-password")
        
        password = generate_password_hash(new_password_initial)

        db_session.execute("UPDATE users SET password =:password WHERE email=:email", {'password':password, 'email':email})
        db_session.commit()

        flash("Success!")

        return redirect("/sign-in")
    else:
        return render_template("change_password.html")

# This is the endpoint for the "Search for Ratings" page.
@bp.route("/search-for-ratings", methods=["GET", "POST"])
def search_for_ratings():
    if request.method == "POST":
        student_organization_name = request.form.get("student_organization_name")
        if not student_organization_name:
            flash("Student organization name field must be completed.")
            return redirect("/search-for-ratings")
        
        student_organization_id = db_session.execute("SELECT id FROM student_organizations WHERE name =:student_organization_name", {'student_organization_name':student_organization_name}).first()
        if not student_organization_id:
            flash("Student organization name is incorrect.")
            return redirect("/search-for-ratings")
        
        racial_identity_ratings = db_session.execute("SELECT racial_identity FROM ratings WHERE racial_identity IS NOT NULL AND student_organization_id =:student_organization_id", {'student_organization_id':student_organization_id})
        ethnic_identity_ratings = db_session.execute("SELECT ethnic_identity FROM ratings WHERE ethnic_identity IS NOT NULL AND student_organization_id =:student_organization_id", {'student_organization_id':student_organization_id})
        gender_identity_ratings = db_session.execute("SELECT gender_identity FROM ratings WHERE gender_identity IS NOT NULL AND student_organization_id =:student_organization_id", {'student_organization_id':student_organization_id})
        sexual_orientation_ratings = db_session.execute("SELECT sexual_orientation FROM ratings WHERE sexual_orientation IS NOT NULL AND student_organization_id =:student_organization_id", {'student_organization_id':student_organization_id})
        socioeconomic_status_ratings = db_session.execute("SELECT socioeconomic_status FROM ratings WHERE socioeconomic_status IS NOT NULL AND student_organization_id =:student_organization_id", {'student_organization_id':student_organization_id})
        religious_identity_ratings = db_session.execute("SELECT religious_identity FROM ratings WHERE religious_identity IS NOT NULL AND student_organization_id =:student_organization_id", {'student_organization_id':student_organization_id})
        disability_identity_ratings = db_session.execute("SELECT disability_identity FROM ratings WHERE disability_identity IS NOT NULL AND student_organization_id =:student_organization_id", {'student_organization_id':student_organization_id})

        array_of_racial_identity_ratings = []
        for row in racial_identity_ratings:
            array_of_racial_identity_ratings.append(row["racial_identity"])
        median_of_racial_identity_ratings = median(array_of_racial_identity_ratings)
        mean_of_racial_identity_ratings = mean(array_of_racial_identity_ratings)
        plt.hist(array_of_racial_identity_ratings)
        plt.savefig('temporary_histograms/histogram_of_racial_identity_ratings.png')

        array_of_ethnic_identity_ratings = []
        for row in ethnic_identity_ratings:
            array_of_ethnic_identity_ratings.append(row["ethnic_identity"])
        median_of_ethnic_identity_ratings = median(array_of_ethnic_identity_ratings)
        mean_of_ethnic_identity_ratings = mean(array_of_ethnic_identity_ratings)
        plt.hist(array_of_ethnic_identity_ratings)
        plt.savefig('temporary_histograms/histogram_of_ethnic_identity_ratings.png')

        array_of_gender_identity_ratings = []
        for row in gender_identity_ratings:
            array_of_gender_identity_ratings.append(row["gender_identity"])
        median_of_gender_identity_ratings = median(array_of_gender_identity_ratings)
        mean_of_gender_identity_ratings = mean(array_of_gender_identity_ratings)
        plt.hist(array_of_gender_identity_ratings)
        plt.savefig('temporary_histograms/histogram_of_gender_identity_ratings.png')
        
        array_of_sexual_orientation_ratings = []
        for row in sexual_orientation_ratings:
            array_of_sexual_orientation_ratings.append(row["sexual_orientation"])
        median_of_sexual_orientation_ratings = median(array_of_sexual_orientation_ratings)
        mean_of_sexual_orientation_ratings = mean(array_of_sexual_orientation_ratings)
        plt.hist(array_of_sexual_orientation_ratings)
        plt.savefig('temporary_histograms/histogram_of_sexual_orientation_ratings.png')
        
        array_of_socioeconomic_status_ratings = []
        for row in socioeconomic_status_ratings:
            array_of_socioeconomic_status_ratings.append(row["socioeconomic_status"])
        median_of_socioeconomic_status_ratings = median(array_of_socioeconomic_status_ratings)
        mean_of_socioeconomic_status_ratings = mean(array_of_socioeconomic_status_ratings)
        plt.hist(array_of_socioeconomic_status_ratings)
        plt.savefig('temporary_histograms/histogram_of_socioeconomic_status_ratings.png')
        
        array_of_religious_identity_ratings = []
        for row in religious_identity_ratings:
            array_of_religious_identity_ratings.append(row["religious_identity"])
        median_of_religious_identity_ratings = median(array_of_religious_identity_ratings)
        mean_of_religious_identity_ratings = mean(array_of_religious_identity_ratings)
        plt.hist(array_of_religious_identity_ratings)
        plt.savefig('temporary_histograms/histogram_of_religious_identity_ratings.png')
        
        array_of_disability_identity_ratings = []
        for row in disability_identity_ratings:
            array_of_disability_identity_ratings.append(row["disability_identity"])
        median_of_disability_identity_ratings = median(array_of_disability_identity_ratings)
        mean_of_disability_identity_ratings = mean(array_of_disability_identity_ratings)
        plt.hist(array_of_disability_identity_ratings)
        plt.savefig('temporary_histograms/histogram_of_disability_identity_ratings.png')
        
        return render_template("ratings.html", student_organization_name=student_organization_name, median_of_racial_identity_ratings=median_of_racial_identity_ratings, mean_of_racial_identity_ratings=mean_of_racial_identity_ratings, median_of_ethnic_identity_ratings=median_of_ethnic_identity_ratings, mean_of_ethnic_identity_ratings=mean_of_ethnic_identity_ratings, median_of_gender_identity_ratings=median_of_gender_identity_ratings, mean_of_gender_identity_ratings=mean_of_gender_identity_ratings, median_of_sexual_orientation_ratings=median_of_sexual_orientation_ratings, mean_of_sexual_orientation_ratings=mean_of_sexual_orientation_ratings, median_of_socioeconomic_status_ratings=median_of_socioeconomic_status_ratings, mean_of_socioeconomic_status_ratings=mean_of_socioeconomic_status_ratings, median_of_religious_identity_ratings=median_of_religious_identity_ratings, mean_of_religious_identity_ratings=mean_of_religious_identity_ratings, median_of_disability_identity_ratings=median_of_disability_identity_ratings, mean_of_disability_identity_ratings=mean_of_disability_identity_ratings)

    else:
        return render_template("search_for_ratings.html")

# This is the endpoint for the "Your Ratings" page.
@bp.route("/your-ratings")
@sign_in_required
def your_ratings():
    rows = db_session.execute("SELECT student_organization_id, racial_identity, ethnic_identity, gender_identity, sexual_orientation, socioeconomic_status, religious_identity, disability_identity FROM ratings WHERE user_id=:user_id", {'user_id':session["user_id"]})
    return render_template("your_ratings.html", rows = rows)

# This is the endpoint for the "Rate" page.
@bp.route("/rate")
@sign_in_required
def rate():
    if request.method == "POST":
        student_organization_name = request.form.get("student_organization_name")
        if not student_organization_name:
            flash("Student organization name field must be completed.")
            return redirect("/rate")
        
        student_organization_id = db_session.execute("SELECT id FROM student_organizations WHERE name =:student_organization_name", {'student_organization_name':student_organization_name}).first()
        if not student_organization_id:
            flash("Student organization name is incorrect.")
            return redirect("/rate")
        
        racial_identity_rating = int(request.form.get("racial_identity_rating"))
        ethnic_identity_rating = int(request.form.get("ethnic_identity_rating"))
        gender_identity_rating = int(request.form.get("gender_identity_rating"))
        sexual_orientation_rating = int(request.form.get("sexual_orientation_rating"))
        socioeconomic_status_rating = int(request.form.get("socioeconomic_status_rating"))
        religious_identity_rating = int(request.form.get("religious_identity_rating"))
        disability_identity_rating = int(request.form.get("disability_identity_rating"))
        
        rating_id = db_session.execute("SELECT id FROM ratings WHERE student_organization_id =:student_organization_id AND user_id=:user_id", {'student_organization_id':student_organization_id, 'user_id':session["user_id"]}).first()
        if rating_id:
            db_session.execute("DELETE FROM ratings WHERE student_organization_id =:student_organization_id AND user_id=:user_id", {'student_organization_id':student_organization_id, 'user_id':session["user_id"]})
        
        rating = Rating(user_id=session["user_id"], student_organization_id=student_organization_id, racial_identity=racial_identity_rating, ethnic_identity=ethnic_identity_rating, gender_identity=gender_identity_rating, sexual_orientation=sexual_orientation_rating, socioeconomic_status=socioeconomic_status_rating, religious_identity=religious_identity_rating, disability_identity=disability_identity_rating)
        db_session.add(rating)
        db_session.commit()

        flash("Success!")

        return redirect("/your-ratings")
    else:
        return render_template("rate.html")
