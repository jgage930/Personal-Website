import email
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ContactMeForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired()])
    email = StringField('Your Email', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    message = StringField('Your Message Here', validators=[DataRequired()])
    submit = SubmitField('Submit')