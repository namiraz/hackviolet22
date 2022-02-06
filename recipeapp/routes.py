from flask import render_template, redirect, session, url_for
from recipeapp import app
from recipeapp.forms import IngredientsListForm

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    form = IngredientsListForm()
    if form.validate_on_submit():
        session["ingredients"] = form.ingredients.data
        session["appliances"] = form.appliances.data
        #API call below this point
        url = "https://tasty.p.rapidapi.com/recipes/list"

        querystring = {"from":"0","size":"5","q":form.ingredients.data}

        headers = {
            'x-rapidapi-host': "tasty.p.rapidapi.com",
            'x-rapidapi-key': "fe5e900e75msh990876c1b7db3bap12a124jsn651c3ff6276b"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        j = response.text
        return redirect(url_for("results"))
    return render_template("home.html", form=form)

@app.route("/results", methods=["GET", "POST"])
def results():
    ingredients = session["ingredients"]
    appliances = session["appliances"]
    return render_template("results.html", ingredients=ingredients, appliances=appliances)

@app.route("/manual", methods=["GET", "POST"])
def manual():
    return render_template("manual.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html")
