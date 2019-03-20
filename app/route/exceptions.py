from flask import render_template
from werkzeug import exceptions

from app import app


@app.errorhandler(exceptions.Unauthorized)
def unauthorized_exception(error):
    return render_template(
        'exception.html',
        code=error.code,
        name=error.name,
        description=error.description
    )


app.register_error_handler(403, unauthorized_exception)
