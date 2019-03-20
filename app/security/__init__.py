from app.security.form import SchedLogin
from app.models.user import UserModel, RoleModel
from flask_security import SQLAlchemyUserDatastore, Security


def enable_security(app, db):
    security = Security()
    datastore = SQLAlchemyUserDatastore(db, UserModel, RoleModel)
    security.init_app(app, datastore=datastore, login_form=SchedLogin)

    return datastore, security
