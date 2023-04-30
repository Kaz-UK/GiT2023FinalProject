from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length
from wtforms.widgets import TextArea


class GameForm(FlaskForm):
    game_name = StringField('Game Name', validators=[DataRequired()])
    num_of_players = IntegerField('Maximum Number of Players', validators=[DataRequired()])
    min_age = IntegerField('Minimum Age', validators=[DataRequired()])
    duration_of_play_time = IntegerField('Duration of Play (min)', validators=[DataRequired()])
    gameplay = SelectField('Game Play', choices=[('competitive', 'competitive'), ('co-operative', 'co-operative')])
    game_description = StringField('Game Description', validators=[Length(max=4000)], widget=TextArea())
    submit = SubmitField('Add Game')
