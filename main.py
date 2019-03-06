from app import create_app, db
from app.admin import setup_admin, enable_security
from app.config import DevConfig

app = create_app(DevConfig)
data_store, _ = enable_security(app)

setup_admin(app)

#
# @app.before_first_request
# def setup_first_run():
#     data_store.create_user(name="admin@sched.hk", password="admin")
#     db.session.commit()


app.run(debug=True)
