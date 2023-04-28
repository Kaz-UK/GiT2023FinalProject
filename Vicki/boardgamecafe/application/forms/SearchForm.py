from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# Navigation form search bar
class SearchForm(FlaskForm):
    searched_game_name = StringField("searched_game_name", validators=[DataRequired()])
    submit = SubmitField("Submit")
