from app import db
from app.models.types import JSON


class RequestActionModel(db.Model):
    __tablename__ = 'request_action'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)

    schema = db.Column(db.String(5), nullable=False)
    url = db.Column(db.String(100), nullable=False)
    method = db.Column(db.String(100), nullable=False)
    headers = db.Column(JSON(255), nullable=True)
    params = db.Column(JSON(255), nullable=True)

    scenario = db.relationship('ScenarioModel', backref='request_action', lazy='dynamic')

    def __str__(self):
        return self.name