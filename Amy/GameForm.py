from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from application.models.game import Game


class GameForm(FlaskForm):
    game_name = StringField('Game Name')
    num_of_players = IntegerField('Num of players')
    min_age = IntegerField('Minimum age')
    duration_of_play_time = IntegerField('Duration of play (mins)')
    gameplay = StringField('Game play')
    game_description = StringField('Game description')
    # DON'T NEED THIS yet -  CAN USE DROP-DOWN FOR GAMEPLAY IN HTML
    # gameplay_list = QuerySelectField(
    #     'Game',
    #     query_factory=lambda: Game.query,
    #     allow_blank=False,
    #     get_label='gameplay'
    # )
    submit = SubmitField('Add Game')