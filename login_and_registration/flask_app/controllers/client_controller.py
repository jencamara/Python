from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt

from flask_app import app
from flask_app.models.client import Client

bcrypt = Bcrypt(app)

@app.route("/")
def index():
    if "copl" in session:
        return redirect("/clients")

    return render_template("index.html")

@app.route("/clients")
def display_client_page():
    if "copl" not in session:
        flash ("you need to sign in to your account")
        return redirect ("/")

    return render_template("client.html", all_clients = Client.get_every(), client = Client.get_single({"id": session['copl']}))

@app.route("/registration", methods = ['POST'])
def create_account():
    if not Client.registration_good(request.form):
        return redirect("/")

    defender = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        "password": defender
    }
    client_id = Client.create(data)

    session["copl"] = client_id

    return redirect("/clients")

@app.route("/signin", methods = ['POST'])
def signin():
    if not Client.login_good(request.form):
        return redirect("/")

    client = Client.select_email({"email":request.form['email']})

    session["copl"] = client.id

    return redirect("/clients")

@app.route("/signout")
def signout():
    session.clear()

    return redirect("/")

