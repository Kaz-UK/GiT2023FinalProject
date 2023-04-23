from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, DateField
from wtforms.ext.sqlalchemy.fields import QuerySelectField


from application.models.cafesession import Cafesession
from application.models.customer import Customer
from application.models.stock import Stock
from application.models.game import Game
import datetime


class BookingForm(FlaskForm):

    game_list = QuerySelectField(
        'Stock',
        query_factory=lambda: Game.query,
        allow_blank=False,
        get_label='game_name'
    )
    session_date_list = QuerySelectField(
        'Cafesession',
        query_factory=lambda: Cafesession.query,
        allow_blank=False,
        get_label='session_date'
    )
    session_list = QuerySelectField(
        'Cafesession',
        query_factory=lambda: Cafesession.query,
        allow_blank=False,
        get_label='session_type'
    )

    email = StringField('Customer email')

    submit = SubmitField('Add Booking')
