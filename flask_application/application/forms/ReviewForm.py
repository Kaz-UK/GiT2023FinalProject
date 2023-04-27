from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField


from application.models.review import Review
from application.models.customer import Customer
from application.models.game import Game
from wtforms.validators import DataRequired, EqualTo, length

class ReviewForm(FlaskForm):

    email = StringField('email address', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    stars = IntegerField('Star Rating', validators=[DataRequired()])
    game_list = QuerySelectField(
        'Game',
        query_factory=lambda: Game.query,
        allow_blank=False,
        get_label='game_name'
    )
    submit = SubmitField('Add Review')
