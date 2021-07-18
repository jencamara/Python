from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo

# this is where app.routes will go
@app.route("/dojos")
def index():
    return render_template("index.html", all_dojos = Dojo.get_every())

@app.route("/dojos/create", methods = ['POST'])
def create_dojo():
    
    Dojo.create(request.form)
    
    return redirect("/dojos")

