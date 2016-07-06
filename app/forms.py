from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired,Length



class Todo_form(Form):
    content = StringField('content', validators=[DataRequired(), Length(max=50)])
    submit = SubmitField('add')