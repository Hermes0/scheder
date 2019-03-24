from app import db


class ScenarioModel(db.Model):
    __tablename__ = 'scenario'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)

    run_count = db.Column(db.Integer, nullable=False, unique=False)
    frequency = db.Column(db.Integer, nullable=True, unique=False)
    owner = db.Column(db.Integer, db.ForeignKey('users.id'))
    schedule = db.Column(db.Integer, db.ForeignKey('schedule.id'))

    def __str__(self):
        return f"{self.id} - {self.name}"
