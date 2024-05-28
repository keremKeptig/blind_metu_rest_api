from database import db


class ScheduleTable(db.Model):
    __tablename__ = "slots"

    day = db.Column(db.String(80), primary_key=True)
    start_time = db.Column(db.Integer, primary_key=True)
    end_time = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), db.ForeignKey("user.username"), primary_key=True, nullable=False)

    # user = db.relationship('UserTable', back_populates='slots', cascade='all, delete')
