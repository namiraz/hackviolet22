from flask import render_template, url_for
from recipeapp import app
from recipeapp.forms import IngredientsListForm

@app.route("/")
@app.route("/home")
def home():
    form = IngredientsListForm()
    return render_template("home.html", form=form)

@app.route("/manual")
def manual():
    return render_template("manual.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
