import logging
import os
import sys

logger = logging.getLogger(__name__)


class AppMode:
    DEV = "dev"
    PROD = "prod"


class Config:
    SECRET_KEY = "somelongsecret"
    FLASK_ADMIN_SWATCH = 'cerulean'
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    SECURITY_PASSWORD_SALT = 'salt'

    @classmethod
    def get_config(cls, mode=None):
        app_mode = mode or os.getenv('APP_MODE')

        if not app_mode:
            raise ValueError("APP_MODE is not set.")

        app_config = {
            AppMode.DEV: DevConfig,
            AppMode.PROD: ProdConfig
        }

        try:
            logger.debug(f"Setup config. Config mode: {app_mode}")
            return app_config.get(app_mode)
        except KeyError:
            sys.exit(33)


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://admin:admin@localhost:5432/sched"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
