from flask import render_template
from flask_security import login_required

from app import app


@app.route("/")
@app.route("/index")
@login_required
def main():
    return render_template("base.html")


@app.route("/add-action")
def add_action():
    return render_template("form.html")


@app.route("/history")
def history():
    return render_template("history.html")
