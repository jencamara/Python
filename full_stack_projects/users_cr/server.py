from flask import Flask, render_template, redirect, request
from user import User

app=Flask(__name__)
app.secret_key = "we keep secrets to keep this safe"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/users/new")
def new_user():
    return render_template("new_user.html")

@app.route("/users/add", methods = ['POST'])
def add_user():
    User.create(request.form)

    return redirect("/")

if __name__=="__main__":
    app.run(debug = True)