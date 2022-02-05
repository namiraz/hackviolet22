from flask import render_template, url_for
from recipeapp import app
from recipeapp.forms import IngredientsListForm

@app.route("/")
@app.route("/home")
def home():
    form = IngredientsListForm()
    return render_template("home.html", form=form)
