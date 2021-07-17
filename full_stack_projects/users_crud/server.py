from flask import Flask, render_template, redirect, request
from user import User

app=Flask(__name__)
app.secret_key = "we keep secrets to keep this safe"

@app.route("/users")
def index():
    return render_template("index.html", all_users=User.get_every())

@app.route("/users/new")
def new_user():
    return render_template("new_user.html")

@app.route("/users/add", methods = ['POST'])
def add_user():
    User.create(request.form)

    return redirect("/users")
    

@app.route("/users/<int:user_id>")
def display_user(user_id):
    return render_template("user.html", user = User.get_single({"id": user_id}))

@app.route("/users/<int:user_id>/edit")
def edit_user(user_id):
    return render_template("edituser.html", user = User.get_single({"id": user_id}))

@app.route("/users/<int:user_id>/update", methods = ["POST"])
def update_user(user_id):
    new_dict = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "id": user_id
    }
    User.update(new_dict)
    return redirect ("/users")

@app.route("/users/<int:user_id>/destroy")
def delete_user(user_id):
    User.delete({"id":user_id})
    return redirect("/users")


if __name__=="__main__":
    app.run(debug = True)