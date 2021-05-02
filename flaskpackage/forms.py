from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField , StringField
from wtforms.validators import DataRequired, Length


class CheckResultForm(FlaskForm):
    result = IntegerField('', validators=[DataRequired()])
    submit = SubmitField('Go!')

class EnterNicknameForm(FlaskForm):
    nickname = StringField('Nickname', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Ok')