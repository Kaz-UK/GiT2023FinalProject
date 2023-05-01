from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
# from application.models.review import Review
# from application.models.customer import Customer
from application.models.game import Game
from wtforms.validators import DataRequired, Length
from wtforms.widgets import TextArea


class ReviewForm(FlaskForm):
    review = StringField('Review', validators=[DataRequired(), Length(max=4000)], widget=TextArea())
    stars = IntegerField('Star Rating', validators=[DataRequired()])
    game_list = QuerySelectField(
        'Game',
        query_factory=lambda: Game.query.order_by(Game.game_name),
        allow_blank=False,
        get_label='game_name'
    )
    submit = SubmitField('Add Review')
