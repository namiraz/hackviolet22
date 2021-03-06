import json
import os
import requests
from flask import render_template, redirect, session, url_for
from recipeapp import app
from recipeapp.forms import IngredientsListForm

tasty_api_key = os.getenv("TASTY_API_KEY")

@app.route("/home", methods=["GET", "POST"])
def home():
    form = IngredientsListForm()
    if form.validate_on_submit():
        session["ingredients"] = form.ingredients.data
        session["recipenumber"] = form.num_of_recipes.data
        #API call below this point
        url = "https://tasty.p.rapidapi.com/recipes/list"

        querystring = {"from":"0","size":form.num_of_recipes.data or "10","q":form.ingredients.data}

        headers = {
            'x-rapidapi-host': "tasty.p.rapidapi.com",
            'x-rapidapi-key': tasty_api_key
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.text
        session["data"] = data
        return redirect(url_for("results"))
    return render_template("home.html", form=form)

@app.route("/results", methods=["GET", "POST"])
def results():
    data = session["data"]
    data = data.encode('utf-8')
    data = json.loads(data.decode('utf-8'))
    recipes = []
    for recipe in data["results"]:
        try:
            info = {}
            info["name"] = recipe["name"]
            info["ingredients"] = []
            info["instructions"] = []
            info["image"] = recipe["thumbnail_url"]
            for components in recipe["sections"]:
                for ingredients in components["components"]:
                    info["ingredients"].append(ingredients["raw_text"])
            for steps in recipe["instructions"]:
                info["instructions"].append(steps["display_text"])
            #print("--------------PP------------")
        except KeyError:
            continue
        recipes.append(info)
    return render_template("results.html", recipes=recipes)

@app.route("/", methods=["GET", "POST"])
@app.route("/manual", methods=["GET", "POST"])
def manual():
    return render_template("manual.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html")
