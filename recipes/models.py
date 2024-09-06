from recipes import db


class Cuisine(db.Model):
    # schema for the Cuisine model
    id = db.Column(db.Integer, primary_key=True)
    cuisine_name = db.Column(db.String(25), unique=True, nullable=False)
    recipes = db.relationship("Recipe", backref="cuisine", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.cuisine_name


class Recipe(db.Model):
    # schema for the Recipe model
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(50), unique=True, nullable=False)
    recipe_description = db.Column(db.Text, nullable=False)
    recipe_duration = db.Column(db.Integer, nullable=False)
    is_vegetarian = db.Column(db.Boolean, default=False, nullable=False)
    cuisine_id = db.Column(db.Integer, db.ForeignKey("cuisine.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Recipe: {1} | Vegetarian: {2}".format(
            self.id, self.recipe_name, self.is_vegetarian
        )