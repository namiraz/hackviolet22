from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, TextAreaField
from wtforms.validators import DataRequired

class IngredientsListForm(FlaskForm):
    ingredients = TextAreaField("Ingredients",
        validators=[DataRequired()]
    )
    appliances = TextAreaField("Appliances",
        validators=[DataRequired()]
    )
    submit = SubmitField("Find Recipes")
