from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField 
from wtforms.fields import TextAreaField
from wtforms.validators import DataRequired, Length


class AddNoteForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=50)])
    text = TextAreaField('Text', validators=[DataRequired(), Length(min=2, max=500)])
    submit = SubmitField('Add')