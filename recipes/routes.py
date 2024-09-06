from flask import render_template
from recipes import app, db
from recipes.models import Cuisine, Recipe


@app.route("/")
def home():
    return render_template("recipes.html")

@app.route("/cuisines")
def cuisines():
    return render_template("cuisines.html")

@app.route("/add_cuisine", methods=["GET", "POST"])
def add_cuisine():
    return render_template("add_cuisine.html")

@app.route("/edit_cuisine/<int:cuisine_id>", methods=["GET", "POST"])
def edit_cuisine():
    return render_template("edit_cuisine.html")

@app.route("/delete_cuisine/<int:cuisine_id>")
def delete_cuisine():
    return render_template("edit_cuisine.html")

@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    return render_template("add_recipe.html")

@app.route("/edit_recipe/<int:recipe_id>", methods=["GET", "POST"])
def edit_recipe():
    return render_template("edit_recipe.html")

@app.route("/delete_recipe/<int:recipe_id>")
def delete_recipe():
    return render_template("edit_recipe.html")