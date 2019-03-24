from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.config import Config

app: Flask = Flask(__name__)
db: SQLAlchemy = SQLAlchemy()
migration: Migrate = Migrate()


def create_app(config_class=None):
    app_config = config_class or Config.get_config()
    app.config.from_object(app_config)

    from app.route import index, auth, exceptions
    from app.models.schedule import ScheduleModel
    from app.models.scenario import ScenarioModel
    from app.models.user import RoleModel, UserModel
    from app.models.action import ActionModel, ActionTypeModel

    db.init_app(app)
    migration.init_app(app, db, directory='app/models/migrations')

    return app
