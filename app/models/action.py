from app import db


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
