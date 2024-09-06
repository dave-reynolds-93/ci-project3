from flask import render_template
from recipes import app, db
from recipes.models import Cuisine, Recipe


@app.route("/")
def home():
    return render_template("base.html")