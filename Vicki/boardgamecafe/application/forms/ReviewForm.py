
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField


from application.models.review import Review
from application.models.customer import Customer
from application.models.game import Game


class ReviewForm(FlaskForm):

    review = StringField('Review')
    stars = IntegerField('Star Rating')
    review_date = StringField('Date')
    customer_id = IntegerField('Customer ID')
    game_id = IntegerField('Game ID')

    customer_list = QuerySelectField(
        'Customer',
        query_factory=lambda: Customer.query,
        allow_blank=False,
        get_label='last_name'
    )

    game_list = QuerySelectField(
        'Game',
        query_factory=lambda: Game.query,
        allow_blank=False,
        get_label='game_name'
    )
    submit = SubmitField('Add Review')
