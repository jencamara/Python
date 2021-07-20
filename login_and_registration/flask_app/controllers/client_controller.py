from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt

from flask_app import app
from flask_app.models.client import Client

bcrypt = Bcrypt(app)

@app.route("/")
def index():
    if "uuid" in session:
        return redirect("/clients")

    return render_template("index.html")

@app.route("/clients")
def display_client_page():
    if "uuid" not in session:
        flash("you need to sign in to your account")
        return redirect ('/')

    return render_template("client.html", all_clients = Client.get_every(), client = Client.get_single({"id": session['uuid']}))

@app.route("/register", methods = ["POST"])
def register():
    if not Client.register_validate(request.form):
        return redirect("/")

    first_defense = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        "password": first_defense
    }
    
    client_id = Client.create(data)

    session["uuid"] = client_id

    return redirect("/clients")

@app.route("/login", methods = ["POST"])
def login():
    if not Client.login_validate(request.form):
        return redirect("/")

    client = Client.select_email({"email": request.form['email']})

    session["uuid"] = client.id

    return redirect("/clients")

@app.route("/signout")
def signout():
    session.clear()

    return redirect("/")

