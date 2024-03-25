from database import db


class MatchTable(db.Model):
    __tablename__ = "matches"

    id = db.Column(db.Integer, primary_key=True)
    user1_id = db.Column(db.String(80), db.ForeignKey("users.username"))
    user2_id = db.Column(db.String(80), db.ForeignKey("users.username"))
    match_date = db.Column(db.Date, nullable=True)
    match_location = db.Column(db.String(256), nullable=False)

    # user = db.relationship('UserTable', back_populates='match')
