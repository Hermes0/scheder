from flask import redirect, url_for, render_template
from flask_login import current_user, login_user
from flask_security import LoginForm

from app import app
from app.models.user import UserModel


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = UserModel.query.filter_by(email=form.email.data).first()

        login_user(user, remember=form.remember.data)
        return redirect(url_for('main'))

    return render_template('security/login_user.html', login_user_form=form)
