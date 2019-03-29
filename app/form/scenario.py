from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired


class ScenarioForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    run_count = IntegerField('Run count', default=0)
    frequency = IntegerField('Frequency run', default=1)



