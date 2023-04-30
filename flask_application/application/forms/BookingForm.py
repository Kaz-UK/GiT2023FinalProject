from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField


from application.models.cafesession import Cafesession
from application.models.customer import Customer
from application.models.stock import Stock
from application.models.game import Game
import datetime
from wtforms.validators import DataRequired


class BookingForm(FlaskForm):

    session_date_list = QuerySelectField(
        'Date/Session',
        query_factory=lambda: Cafesession.query,
        allow_blank=False,
        get_label=lambda s: '%s %s (Available Tables: %s)' % (s.session_date, s.session_type, s.table_count)
    )

    game_list = QuerySelectField(
        'Reserve a game (optional)',
        query_factory=lambda: Game.query,
        allow_blank=True,
        get_label='game_name'
    )

    email = StringField('Customer email', validators=[DataRequired()])

    submit = SubmitField('Book')
