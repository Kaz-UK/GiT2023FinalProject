from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired


class GameForm(FlaskForm):
    game_name = StringField('Game Name', validators=[DataRequired()])
    num_of_players = IntegerField('Number of Players', validators=[DataRequired()])
    min_age = IntegerField('Minimum Age', validators=[DataRequired()])
    duration_of_play_time = IntegerField('Duration of Play (min)', validators=[DataRequired()])
    gameplay = SelectField('Game Play', choices=[('competitive', 'competitive'), ('co-operative', 'co-operative')])
    game_description = StringField('Game Description')
    submit = SubmitField('Add Game')
