from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField 
from wtforms.validators import DataRequired


class checkResultForm(FlaskForm):
    result = IntegerField('', validators=[DataRequired()])
    submit = SubmitField('Go!')