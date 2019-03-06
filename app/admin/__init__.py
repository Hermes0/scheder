from app import db
from flask_admin import Admin
from app.models.action import *
from app.models.user import *
from flask_admin.contrib.sqla import ModelView
from flask_security import SQLAlchemyUserDatastore, Security


def enable_security(app):
    datastore = SQLAlchemyUserDatastore(db, UserModel, RoleModel)
    security = Security(app, datastore)

    return datastore, security


def setup_admin(app):
    admin = Admin(app, name='sched', template_mode='bootstrap3')
    admin.add_view(ModelView(ActionModel, db.session))
    admin.add_view(ModelView(ActionTypeModel, db.session))

    admin.add_view(ModelView(RoleModel, db.session))
    admin.add_view(ModelView(UserModel, db.session))
