from flask import Flask

from app import create_app, db
from app.admin import setup_admin
from app.config import DevConfig
from app.security import enable_security

app: Flask = create_app(DevConfig)
data_store, _ = enable_security(app, db)
setup_admin(app)

from cmd import create_admin

if __name__ == "__main__":
    _ = create_admin
    app.run(debug=True)
