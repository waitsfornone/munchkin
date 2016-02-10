from flask_wtf import Form
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import (DataRequired, ValidationError)

def level_check(form, field):
    if field.data > 10:
        raise ValidationError('''Max player level is 10!
                                Please enter your level again.''')

class PlayerForm(Form):
    name = StringField('Player Name', validators=[DataRequired()])
    level = IntegerField('Player Level', validators=[DataRequired(), level_check],
                            default=1)
    race = StringField('Race', validators=[DataRequired()], default='Human')
    gender = SelectField('Gender', choices=[('m','Male'),('f','Female')])
