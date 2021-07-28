from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.store import Store

# this is where app.routes will go
@app.route("/")
def index():
    return render_template("index.html", all_stores = Store.get_every())

@app.route("/stores/create", methods = ['POST'])
def create_store():
    
    Store.create(request.form)
    
    return redirect("/")

# displays a single store
@app.route("/stores/<int:store_id>")
def display_store(store_id):
    return render_template("store.html", store = Store.get_single({"id": store_id}))


@app.route("/stores/<int:store_id>/delete")
def delete_store(store_id):
    Store.delete({"id":store_id})
    return redirect("/")
