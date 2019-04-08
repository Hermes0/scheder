import sys
import click
from flask_security.utils import hash_password

from app import app, db
from app.models.user import UserModel, RoleModel
from main import data_store


@app.cli.command(short_help='Add admin user.')
@click.argument("email", required=True)
@click.argument("password", required=True)
def create_admin(email, password):
    user = UserModel.query.filter_by(email=email).first()

    if user:
        print(f"ERROR:: User with email {email} already exists. Pick new one.")
        sys.exit(1)

    role = RoleModel.query.filter_by(name="ADMIN").first()

    if not role:
        data_store.create_role(
            name="ADMIN", description="Main role."
        )
        db.session.commit()
        role = RoleModel.query.filter_by(name="ADMIN").first()

    data_store.create_user(
        email=email, password=hash_password(password), roles=[role], active=True
    )
    db.session.commit()
    print("Success.")

