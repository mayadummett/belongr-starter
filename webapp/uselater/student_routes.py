import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from webapp.database import Club, Tag, ClubTag, db_session
from webapp.database import User

bp = Blueprint('students', __name__, url_prefix='/')

@bp.route("/clubpage", methods=["GET", "POST"])
def clubpage():
    clublist = Club.query.all()
    clublength = len(clublist)
    return render_template("clubpage.html", clublist=clublist, clublength=clublength)

@bp.route("/searchtitle", methods=["GET", "POST"])
def searchtitle():
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        title = request.form.get("title")
        search = "%{}%".format(title)
        clublist = Club.query.filter(Club.title.like(search)).all()
        clublength = len(clublist)
        return render_template("clubpage.html", clublist=clublist, clublength=clublength)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("searchtitle.html")

@bp.route("/searchtag", methods=["GET", "POST"])
def searchtag():
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        tag = request.form.get("tag")
        tag_id = Tag.query.filter_by(name=tag).first().id
        club_id = ClubTag.query.filter_by(tag_id = tag_id).first().id
        clublist = Club.query.filter_by(id=club_id).all()
        clublength = len(clublist)
        return render_template("clubpage.html", clublist=clublist, clublength=clublength)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        taglist = Tag.query.all()
        taglength = len(taglist)
        return render_template("searchtag.html", taglist=taglist, taglength=taglength)
