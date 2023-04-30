from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, DateField
from wtforms.ext.sqlalchemy.fields import QuerySelectField


from application.models.cafesession import Cafesession
from application.models.customer import Customer
from application.models.stock import Stock
from application.models.game import Game
import datetime
from wtforms.validators import DataRequired


class BookingForm(FlaskForm):

    game_list = QuerySelectField(
        'Reserve a game (optional)',
        query_factory=lambda: Game.query,
        allow_blank=False,
        get_label='game_name'
    )
    session_date_list = QuerySelectField(
        'Date',
        query_factory=lambda: Cafesession.query,
        allow_blank=False,
        get_label='session_date'
    )

    session_list = SelectField(
        'Session', choices=[('Lunchtime', 'Lunchtime'), ('Afternoon', 'Afternoon'), ('Evening', 'Evening')]
    )
    email = StringField('Customer email', validators=[DataRequired()])

    submit = SubmitField('Book')