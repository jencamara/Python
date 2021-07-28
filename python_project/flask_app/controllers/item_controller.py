from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.store import Store
from flask_app.models.item import Item


@app.route("/items")
def new_item():
    return render_template("new_item.html", all_stores = Store.get_every())

@app.route("/items/create", methods = ['POST'])
def create_item():
    Item.create(request.form)

    return redirect(f"/stores/{request.form['store_id']}")

@app.route("/items/<int:id>")
def show_item(id):
    return render_template(
        "item.html",
        item = Item.get_single({"id": id})
        
    )

@app.route("/items/<int:id>/edit")
def edit_item(id):
    return render_template("edit_item.html", item = Item.get_single({"id": id}))

@app.route("/items/<int:id>/update", methods = ['POST'])
def item_update(id):
    post_data ={
        **request.form,
        "id": id
    }
    Item.update(post_data)

    return redirect("/")



@app.route("/items/<int:id>/delete")
def delete_item(id):
    Item.delete({"id": id})

    return redirect ("/")