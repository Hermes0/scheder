from flask_security import RoleMixin, UserMixin

from app import db


class RoleModel(db.Model, RoleMixin):
    __tablename__ = "roles"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name


class UserModel(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(255), unique=True)
    active = db.Column(db.Boolean())
    password = db.Column(db.String(255))

    roles = db.relationship('RoleModel', secondary="users_roles",
                            backref=db.backref('users', lazy='dynamic'))
    scenarios = db.relationship('ScenarioModel', backref='scenario_owner', lazy='dynamic')

    def __str__(self):
        return self.email

    def is_admin(self) -> bool:
        admin_role = RoleModel.query.filter_by(name="ADMIN").first()
        if admin_role:
            return self.has_role(admin_role)

        return False

    def has_role(self, role: RoleModel) -> bool:
        user_role = UserRoles.query.filter_by(user_id=self.id).first()
        if user_role:
            if user_role.role_id == role.id:
                return True

        return False


class UserRoles(db.Model):
    __tablename__ = "users_roles"
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
