from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo, InputRequired, Length


# Registration Form
class RegistrationForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired(), Length(max=50)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(max=50)])
    email = StringField("Email", validators=[InputRequired(), Length(max=50)])
    phone_number = StringField("Phone", validators=[Length(max=20)])
    customer_password = PasswordField("Password", [InputRequired(), EqualTo("confirm_customer_password", message="Password does not match"), Length(max=30)])
    confirm_customer_password = PasswordField("Confirm Password")
    submit = SubmitField("Submit Registration")
