import os

from flask import Flask

app = Flask(__name__)
secret_key = os.getenv("SECRET_KEY")
app.config["SECRET_KEY"] = secret_key

from recipeapp import routes
