from database import db


class ScheduleTable(db.Model):
    __tablename__ = "schedules"

    schedule_id = db.Column(db.Integer, primary_key=True)
    # slots = db.Column(db.Integer, db.ForeignKey("slots.slot_id"), unique=False, nullable=False)
    slots = db.Column(db.Integer, unique=False, nullable=False)

    # users = db.relationship('UserTable', back_populates='schedules', cascade='all, delete')


