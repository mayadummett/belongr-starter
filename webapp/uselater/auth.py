import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, Flask
)
from werkzeug.security import check_password_hash, generate_password_hash
from webapp.database import db_session
from .database import User, ClubLeader, Club, Signup

#supposed to import flask mail
from flask_mail import Mail, Message

#configure mail application
app = Flask(__name__)
app.config['MAIL_USERNAME'] = 't4sgedu@gmail.com'
app.config['MAIL_PASSWORD'] = 'education123!'
app.config['MAIL_PORT'] = 587
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_USE_TLS'] = True
mail = Mail(app)

bp = Blueprint('auth', __name__, url_prefix='/')

@bp.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    # u = User('Bob', 'Jones', 'bob@gmail.com', 'user_bob', 'password')
    # u = User(first_name='Bob', last_name='Jones', email='bob@gmail.com', username='user_bob', password='password')
    # db_session.add(u)
    # db_session.commit()

    print(User.query.all())
    
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        
        # Ensure username was submitted
        if not request.form.get("username"):
            return
            # return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return
            # return apology("must provide password", 403)

        # Query database for username
        rows = User.query.filter_by(username=request.form.get("username")).all()
        print (rows)

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0].password, request.form.get("password")):
            return
            # return apology("invalid username and/or password", 403)
        
        # Remember which user has logged in
        session["user_id"] = rows[0].id

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@bp.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@bp.route("/register", methods=["GET", "POST"])
def register():
    session.clear()
    if request.method == "POST":
            # for the code for this, I am assuming that the user has accurately entered info b/c idk what
            # logic to include in case the user has left the username box blank for example
        
        # Create variables to get the data from the registration form
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        
        # Ensure that the password is the same as the confirmation
        if password == confirmation:
            
            # Generate a hash to store into the database
            hash = generate_password_hash(password)
            
            # Create a newUser variable that stores the user object
            newUser = User(first_name=firstname, last_name=lastname, email=email, username=username, password=hash)
            
            # Add the newUser object to the database
            db_session.add(newUser)
           
            # Update the database
            db_session.commit()

            #creates a message variable that stores the message, sender and recipient of the email
            msg = Message("Thank you for registering for Crimson ClubHouse",
            sender="t4sgedu@gmail.com", recipients=[newUser.email])

            #sends the email to newly registered users
            mail.send(msg)
        return redirect("/login")

    else:
        return render_template("register.html")

# This is for club leaders
@bp.route("/clubleader", methods=["GET", "POST"])
def clubleader():
    if request.method == "POST":
        # Creates variables to get data from club leader form
        clubtitle = request.form.get("clubtitle")

        # Creates a newClubLeader variable that stores the ClubLeader object
        newClubLeader = ClubLeader(user_id=User.id, club_id=Club.query.filter_by(title=clubtitle).first().id)
        
        # Add the newClubLeader object to the database
        db_session.add(newClubLeader)

        # Update the database
        db_session.commit()
        return redirect("/")

    else:
        return render_template("clubleader.html")

@bp.route("/adduser", methods=["GET", "POST"])
def adduser():
    if request.method == "POST":
        # Create variables to get data from club leader form
        clubtitle = request.form.get("clubtitle")
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")

        # Create a newUser variable that stores the newly created Signup Object
        newUser = Signup(user_id=User.query.filter_by(first_name=firstname, last_name=lastname), club_id=Club.query.filter_by(title=clubtitle).first().id)

        # Add the newUser object to the databse
        db_session.add(newUser)

        # Update the database
        db_session.commit()
        return redirect("/")
    
    else:
        return render_template("adduser.html")

# Allow user to change password
@bp.route("/changepw", methods=["GET", "POST"])
def changepw():

    if request.method == "POST": 

        # Ensure password was submitted
        if not request.form.get("password"): 
            return 
        
        # Ensure password matches confirmation password
        elif (request.form.get("password") != request.form.get("confirmation")):
            return 
        
        # All conditions are met — password submitted + matches confirmation
        else: 
            # Hash user's password
            hash = generate_password_hash(request.form.get("password"))
            user_id = session["user_id"]
            
            # Update database to reflect new password
            session.query(User).filter(id=user_id).update({"password": hash},synchronize_session=False)
            
            # db.execute("UPDATE users SET password = ? WHERE id = ?", hash, user_id)
            # db_session.commit()

            # Redirect user to home page 
            return redirect("/")
    
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("changepw.html")