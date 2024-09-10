from flask import render_template, request, redirect, url_for
from recipes import app, db
from recipes.models import Cuisine, Recipe


@app.route("/")
def home():
    recipes = list(Recipe.query.order_by(Recipe.id).all())
    return render_template("recipes.html", recipes=recipes)

@app.route("/cuisines")
def cuisines():
    cuisines = list(Cuisine.query.order_by(Cuisine.cuisine_name).all())
    return render_template("cuisines.html", cuisines=cuisines)

@app.route("/add_cuisine", methods=["GET", "POST"])
def add_cuisine():
    if request.method == "POST":
        cuisine = Cuisine(cuisine_name=request.form.get("cuisine_name"))
        db.session.add(cuisine)
        db.session.commit()
        return redirect(url_for("cuisines"))
    return render_template("add_cuisine.html")

@app.route("/edit_cuisine/<int:cuisine_id>", methods=["GET", "POST"])
def edit_cuisine(cuisine_id):
    cuisine = Cuisine.query.get_or_404(cuisine_id)
    if request.method == "POST":
        cuisine.cuisine_name = request.form.get("cuisine_name")
        db.session.commit()
        return redirect(url_for("cuisines"))
    return render_template("edit_cuisine.html", cuisine=cuisine)

@app.route("/delete_cuisine/<int:cuisine_id>")
def delete_cuisine(cuisine_id):
    cuisine = Cuisine.query.get_or_404(cuisine_id)
    db.session.delete(cuisine)
    db.session.commit()
    return redirect(url_for("cuisines"))

@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    cuisines = list(Cuisine.query.order_by(Cuisine.cuisine_name).all())
    if request.method == "POST":
        recipe = Recipe(
            recipe_name=request.form.get("recipe_name"),
            recipe_description=request.form.get("recipe_description"),
            is_vegetarian=bool(True if request.form.get("is_vegetarian") else False),
            recipe_duration=request.form.get("recipe_duration"),
            cuisine_id=request.form.get("cuisine_id")
        )
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_recipe.html", cuisines=cuisines)

@app.route("/edit_recipe/<int:recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    cuisines = list(Cuisine.query.order_by(Cuisine.cuisine_name).all())
    if request.method == "POST":
        recipe.recipe_name = request.form.get("recipe_name")
        recipe.recipe_description = request.form.get("recipe_description")
        recipe.is_vegetarian = bool(True if request.form.get("is_vegetarian") else False)
        recipe.duration = request.form.get("duration")
        recipe.cuisine_id = request.form.get("cuisine_id")
        db.session.commit()
    return render_template("edit_recipe.html", recipe=recipe, cuisines=cuisines)

@app.route("/delete_recipe/<int:recipe_id>")
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for("home"))