from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, DateField
from wtforms.ext.sqlalchemy.fields import QuerySelectField

import datetime
from wtforms.validators import DataRequired, EqualTo, length

class SessionForm(FlaskForm):
    session_type = SelectField('Type of session',choices=[('Lunchtime', 'Lunchtime'),('Afternoon', 'Afternoon'), ('Evening', 'Evening') ], validators=[DataRequired()])
    session_date = DateField('Date', validators=[DataRequired()])
    table_count = IntegerField('Number of tables', validators=[DataRequired()])
    submit = SubmitField('Add session')