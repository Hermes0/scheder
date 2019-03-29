from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField


class PeriodicityTypeForm(FlaskForm):
    name = StringField('Name')


class ScheduleForm(FlaskForm):
    name = StringField('Name')
    description = StringField('Description')
    type = SelectField('Periodicity type', choices=[])
    run_time = DateField('Run date')
