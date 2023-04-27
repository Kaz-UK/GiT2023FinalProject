from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo


# Registration Form
class RegistrationForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    phone_number = StringField("Phone")
    customer_password = PasswordField("Password", validators=[DataRequired(), EqualTo("confirm_customer_password", message="Password does not match")])
    confirm_customer_password = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Submit Registration")
