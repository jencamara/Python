from flask import render_template, redirect, request, session, flash

from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

# where the app routes will go for recipes
#copl = clients own personal login

@app.route("/home")
def home():
    if "copl" not in session:
        return redirect ("/")

    return render_template(
        "home.html",
        registered_user = User.pull_from_id({"id": session['copl']}),
        every_recipes = Recipe.get_every()
    )

@app.route("/recipes/new")
def add_new_recipe():
    if "copl" not in session:
        return redirect ("/")

    return render_template("new_recipe.html", registered_user = User.pull_from_id({"id": session['copl']}))

@app.route("/recipes/<int:id>")
def show_recipe(id):
    if "copl" not in session:
        return redirect("/")
    
    return render_template(
        "recipe.html",
        registered_user = User.pull_from_id({"id": session['copl']}),
        recipe = Recipe.get_single({"id": id})
        
    )

@app.route("/recipes/make", methods = ['POST'])
def make_recipe():
    if not Recipe.validate(request.form):
        return redirect("/recipes/new")
    
    post_data = {
        **request.form,
        "user_id": session['copl']
    }
    Recipe.create(post_data)

    return redirect("/home")

@app.route("/recipes/<int:id>/update", methods = ['POST'])
def recipe_update(id):
    if not Recipe.validate(request.form):
        return redirect(f"/recipes/{id}/edit")
    
    post_data ={
        **request.form,
        "id": id
    }
    Recipe.update(post_data)

    return redirect("/home")

@app.route("/recipes/<int:id>/edit")
def recipe_edit(id):
    if "copl" not in session:
        return redirect ("/")
    
    recipe = Recipe.get_single({"id": id})

    if session['copl'] != recipe.user.id:
        flash("sorry! this recipe can't be changed")
        return redirect ("/home")

    return render_template(
        "edit_recipe.html",
        registered_user = User.pull_from_id({"id": session ['copl']}),
        recipe = recipe
    )

@app.route("/recipes/<int:id>/delete")
def delete_recipe(id):
    recipe = Recipe.get_single({"id": id})

    if session['copl'] != recipe.user.id:
        flash("sorry! you cant erase this recipe")
        return redirect ("/home")


    Recipe.delete({"id": id})

    return redirect ("/home")