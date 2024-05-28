from database import db


class MatchTable(db.Model):
    __tablename__ = "match"

    id = db.Column(db.Integer, primary_key=True)
    user1_username = db.Column(db.String(80), db.ForeignKey("user.username"))
    user2_username = db.Column(db.String(80), db.ForeignKey("user.username"))
    date = db.Column(db.Date, nullable=True)
    location = db.Column(db.String(256), nullable=False)

    # user1 = db.relationship('UserTable', foreign_keys=[user1_username], back_populates='matches1')
    # user2 = db.relationship('UserTable', foreign_keys=[user2_username], back_populates='matches2')
