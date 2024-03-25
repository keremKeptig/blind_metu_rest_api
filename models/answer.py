from database import db


class AnswerTable(db.Model):
    __tablename__ = "answers"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(80), db.ForeignKey("users.username"))
    q_id = db.Column(db.Integer, db.ForeignKey("questions.q_id"))
    choice = db.Column(db.String(2), nullable=False)

    # user = db.relationship('UserTable', back_populates='answer')
