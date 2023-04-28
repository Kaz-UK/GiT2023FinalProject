from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, DateField
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from application.models.customer import Customer
import datetime
from wtforms.validators import DataRequired, EqualTo, length


class CustomerDetailsForm(FlaskForm):
    email = StringField('Customer email', validators=[DataRequired()])