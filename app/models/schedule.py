from app import db


class PeriodicityTypeModel(db.Model):
    __tablename__ = 'periodicity_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)

    db.relationship('ScheduleModel', backref='type', lazy='dynamic')

    def __str__(self):
        return self.name


class ScheduleModel(db.Model):
    __tablename__ = 'schedule'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    periodicity_type = db.Column(db.Integer, db.ForeignKey('periodicity_type.id'))
    run_time = db.Column(db.Date, nullable=True, unique=True)

    scenario = db.relationship('ScenarioModel', backref='scenario_schedule', lazy='dynamic')

    def __str__(self):
        return f"{self.id} - {self.name}"
