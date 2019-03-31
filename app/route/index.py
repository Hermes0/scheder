from flask import render_template
from flask_security import login_required, current_user

from app import app
from app.form.schedule import ScheduleForm
from app.models.action import RequestActionModel
from app.models.scenario import ScenarioModel
from app.models.schedule import PeriodicityTypeModel, ScheduleModel


@app.route("/")
@app.route("/index")
@login_required
def main():
    return render_template(
        "base.html",
        user=current_user,
        is_admin=current_user.is_admin()
    )


@app.route("/settings")
def settings():
    schedules = ScheduleModel.query.all()
    schedule_form = ScheduleForm()
    schedule_form.type.choices = [
        (p_type.id, p_type.name) for p_type in PeriodicityTypeModel.query.all()
    ]

    request_actions = RequestActionModel.query.all()

    return render_template(
        "form.html",
        user=current_user,
        actions=request_actions,
        schedules=schedules,
        schedule_form=schedule_form
    )


@app.route("/scenarios")
def scenarios():
    user_scenarios = ScenarioModel.query.filter_by(owner=current_user.id).all()

    return render_template(
        "scenarios.html",
        user=current_user,
        scenarios=user_scenarios
    )
