import os

from flask import Flask
from flask_session import Session

app = Flask(__name__)
secret_key = os.getenv("SECRET_KEY")
app.config["SECRET_KEY"] = secret_key

SESSION_TYPE = "filesystem"
app.config.from_object(__name__)
Session(app)

from recipeapp import routes
