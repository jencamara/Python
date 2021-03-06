from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/ninjas/display")
def show_ninjas():
    return render_template("ninja.html", all_ninjas = Ninja.get_every())

@app.route("/ninjas")
def new_ninja():
    return render_template("new_ninja.html", all_dojos = Dojo.get_every())

@app.route("/ninjas/create", methods = ['POST'])
def create_ninja():
    Ninja.create(request.form)

    return redirect("/ninjas/display")