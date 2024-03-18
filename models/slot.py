from database import db


class SlotTable(db.Model):
    __tablename__ = "slots"

    slot_id = db.Column(db.Integer, primary_key=True)
    slots = db.Column(db.Integer, db.ForeignKey("slots.slot_id"), unique=False, nullable=False)

    schedule_id = db.Column(db.Integer, db.ForeignKey("schedule.schedule_id"), unique=False, nullable=False)

