from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired,Length
from flask_wtf import FlaskForm

class SigninForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(1,20)])
    username2 = StringField('2', validators=[DataRequired(), Length(1, 20)])
    username3 = StringField('3', validators=[DataRequired(), Length(1, 20)])
    username4 = StringField('4', validators=[DataRequired(), Length(1, 20)])
    username5 = StringField('5', validators=[DataRequired(), Length(1, 20)])
    username6 = StringField('6', validators=[DataRequired(), Length(1, 20)])
    username7 = StringField('7', validators=[DataRequired(), Length(1, 20)])
    username8 = StringField('8', validators=[DataRequired(), Length(1, 20)])
    # submit1 = SubmitField('Sign in')