from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_security import current_user

from app.models.action import *
from app.models.scenario import ScenarioModel
from app.models.schedule import *
from app.models.user import *


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_admin()


def setup_admin(app):
    admin = Admin(app, name='sched', template_mode='bootstrap3', index_view=MyAdminIndexView())
    admin.add_view(ModelView(ActionModel, db.session))
    admin.add_view(ModelView(ActionTypeModel, db.session))

    admin.add_view(ModelView(RoleModel, db.session))
    admin.add_view(ModelView(UserModel, db.session))

    admin.add_view(ModelView(ScenarioModel, db.session))
    admin.add_view(ModelView(ScheduleModel, db.session))
    admin.add_view(ModelView(PeriodicityTypeModel, db.session))
