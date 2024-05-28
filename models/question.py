from database import db


class QuestionTable(db.Model):
    __tablename__ = "questions"
    question_id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(256), unique=False, nullable=False)
    test_id = db.Column(db.Integer, db.ForeignKey("test.test_id"), unique=False, nullable=False)

    # test = db.relationship("TestTable", back_populates="questions")
    # answers = db.relationship('AnswerTable', back_populates='question', cascade='all, delete')

