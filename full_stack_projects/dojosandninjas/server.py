from flask import Flask, render_template, redirect, request
from dojo import Dojo

app = Flask (__name__)
app.secret_key = "keep it secret, keep it safe"

@app.route("/dojos")
def index():
    return render_template("index.html", all_dojos = Dojo.get_every())

@app.route("/dojos/create", methods = ['POST'])
def create_dojo():
    
    Dojo.create(request.form)
    
    return redirect("/dojos")

@app.route("/ninjas")
def new_ninja():
    return render_template("new_ninja.html")


if __name__ == "__main__":
    app.run(debug = True)