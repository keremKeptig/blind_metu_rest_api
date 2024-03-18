from database import db


class QuestionTable(db.Model):
    __tablename__ = "questions"

    q_id = db.Column(db.Integer, primary_key=True)
    q_text = db.Column(db.String(256), unique=False, nullable=False)

    choice1 = db.Column(db.String(100), nullable=True)
    choice2 = db.Column(db.String(100), nullable=True)
    choice3 = db.Column(db.String(100), nullable=True)
    choice4 = db.Column(db.String(100), nullable=True)
    choice5 = db.Column(db.String(100), nullable=True)

    test_id = db.Column(db.Integer, db.ForeignKey("tests.test_id"), unique=False, nullable=False)

    # test = db.relationship("TestTable", back_populates="questions")
    # user = db.relationship("UserTable", back_populates="questions")
    #
