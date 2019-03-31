from flask import render_template
from flask_security import login_required, current_user

from app import app
from app.form.schedule import ScheduleForm
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


@app.route("/test")
def tests():
    form = ScheduleForm()

    form.type.choices = [
        (ptype.id, ptype.name) for ptype in PeriodicityTypeModel.query.all()
    ]

    return render_template("test.html", form=form, user=current_user)


@app.route("/scenarios")
def scenarios():
    schedules = ScheduleModel.query.all()
    schedule_form = ScheduleForm()
    schedule_form.type.choices = [
        (p_type.id, p_type.name) for p_type in PeriodicityTypeModel.query.all()
    ]

    return render_template(
        "form.html",
        user=current_user,
        schedules=schedules,
        schedule_form=schedule_form
    )


@app.route("/add-schedule", methods=['POST'])
def add_schedule():
    pass


@app.route("/history")
def history():
    return render_template("history.html", user=current_user)
