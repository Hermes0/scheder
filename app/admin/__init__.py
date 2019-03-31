from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_security import current_user

from app.models.action import RequestActionModel
from app.models.scenario import ScenarioModel
from app.models.schedule import *
from app.models.user import *


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_admin()


def setup_admin(app):
    admin = Admin(app, name='sched', template_mode='bootstrap3', index_view=MyAdminIndexView())

    admin.add_view(ModelView(RoleModel, db.session, category='Users', name='Roles'))
    admin.add_view(ModelView(UserModel, db.session, category='Users', name='Users'))

    admin.add_view(
        ModelView(ScenarioModel, db.session, category='Scenarios', name='Scenarios')
    )
    admin.add_view(ModelView(RequestActionModel, db.session, category='Scenarios', name='Actions'))

    admin.add_view(ModelView(ScheduleModel, db.session, category='Schedules', name='Schedules'))
    admin.add_view(ModelView(
        PeriodicityTypeModel, db.session, category='Schedules', name='Periodicity types')
    )
