import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from webapp.database import db_session
from webapp.database import User
from sqlalchemy import delete
from sqlalchemy import insert

bp = Blueprint('stars', __name__, url_prefix='/')

@bp.route("/starclub", methods=["GET", "POST"])
def cart():
    # POST
    if request.method == "POST":
        clubid = request.form.get("id")
        u = User.query.filter_by(id=session["user_id"]).first()
        rows = Signup.query.filter_by(user_id = u.id, club_id = clubid).first()
        if len(rows) != 0:
            # they already starred the club, so unstar 
            db_session.delete(rows)
            db_session.commit()
        star = Signup(user_id = u.id, club_id = clubid)
        db_session.add(star)
        db_session.commit()
    return render_template("star.html")

    # GET
    # was throwing error so commented out
    # clubs = db.select([Signup]).where(Signup.columns.user_id = u.id)
    return render_template("star.html", clubs=clubs)


@bp.route("/calendar", methods=["GET", "POST"])
def calendar():
    # POST
    if request.method == "POST":
        eventid = request.form.get("id")
        u = User.query.filter_by(id=session["user_id"]).first()
        # was throwing error so commented out
        # rows = Calendar.query.filter_by(user_id = u.id, event_id = eventid).first()
        if len(rows) != 0:
            # they already starred the event, so unstar 
            db_session.delete(rows)
            db_session.commit()
        star = Calendar(user_id = u.id, event_id = eventid)
        db_session.add(star)
        db_session.commit()
        return redirect("/clubcart")

    # GET
    # was throwing error so commented out
    # events = db.select([Calendar]).where(Calendar.columns.user_id = u.id)
    return render_template("calendar.html", events = events)