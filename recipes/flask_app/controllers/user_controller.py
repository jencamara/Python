from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt

from flask_app import app
from flask_app.models.user import User

bcrypt = Bcrypt(app)

@app.route("/")
def index():
    if "copl" in session:
        return redirect("/home")
    #copl = clients own personal login
    return render_template("index.html")

# @app.route("/home")
# def display_home():
#     if "copl" not in session:
#         flash("you need to sign in to your account")
#         return redirect ('/')

#     return render_template("home.html", registered_users = User.get_all(), user = User.get_by_id({"id": session['copl']}))

@app.route("/signup", methods = ["POST"])
def signup():
    if not User.signup_validate(request.form):
        return redirect("/")

    first_defense = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        "password": first_defense
    }
    
    user_id = User.create(data)

    session["copl"] = user_id

    return redirect("/home")

@app.route("/signin", methods = ["POST"])
def signin():
    if not User.signin_validate(request.form):
        return redirect("/")

    user = User.pull_from_email({"email": request.form['email']})

    session["copl"] = user.id

    return redirect("/home")

@app.route("/signout")
def signout():
    session.clear()

    return redirect("/")
