from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField


from application.models.cafesession import Cafesession
from application.models.customer import Customer
from application.models.stock import Stock


class BookingForm(FlaskForm):

    stock_id = IntegerField('Stock ID')
    session_id = IntegerField('Session ID')
    customer_id = StringField('Customer ID')
    number_of_tables = IntegerField('Number of Tables')

    session_list = QuerySelectField(
        'Cafesession',
        query_factory=lambda: Cafesession.query,
        allow_blank=False,
        get_label='session_type'
    )

    customer_list = QuerySelectField(
        'Customer',
        query_factory=lambda: Customer.query,
        allow_blank=False,
        get_label='customer_id'
    )

    stock_list = QuerySelectField(
        'Stock',
        query_factory=lambda: Stock.query,
        allow_blank=False,
        get_label='stock_id'
    )
    submit = SubmitField('Add Booking')
