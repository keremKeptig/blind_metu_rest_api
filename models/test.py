from database import db


class TestTable(db.Model):
    __tablename__ = "tests"

    test_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(80), unique=False, nullable=False)
    test_date = db.Column(db.String(256), nullable=False)

    questions = db.relationship("QuestionsTable", back_populates="tests", lazy="dynamic", cascade="all, delete")


