from database import db


class AnswerTable(db.Model):
    __tablename__ = "answer"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), db.ForeignKey("user.username"))
    question_id = db.Column(db.Integer, db.ForeignKey("questions.question_id"))
    choice = db.Column(db.String(2), nullable=False)

    # user = db.relationship('UserTable', back_populates='answers')
    # question = db.relationship('QuestionTable', back_populates='answers')
