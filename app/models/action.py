from sqlalchemy.types import TypeDecorator, VARCHAR
import json
from app import db


class JSON(TypeDecorator):
    """Represents an immutable structure as a json-encoded string.

    Usage::

        JSONEncodedDict(255)

    """

    impl = VARCHAR

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = json.dumps(value)

        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = json.loads(value)
        return value


class RequestActionModel(db.Model):
    __tablename__ = 'request_action'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)

    schema = db.Column(db.String(5), nullable=False)
    url = db.Column(db.String(100), nullable=False)
    method = db.Column(db.String(100), nullable=False)
    headers = db.Column(JSON(255), nullable=True)


class ActionModel(db.Model):
    __tablename__ = 'action'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    action_type_id = db.Column(db.Integer, db.ForeignKey("action_type.id"))
    settings = None

    action_type = db.relationship("ActionTypeModel", backref="action")

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Action::{self.id}/{self.name}"


class ActionTypeModel(db.Model):
    __tablename__ = 'action_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Action-type:: {self.id}/{self.name}"
