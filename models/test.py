from database import db


class TestTable(db.Model):
    __tablename__ = "tests"

    test_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(80), unique=False, nullable=False)
    test_start_date = db.Column(db.Date, nullable=True)
    test_end_date = db.Column(db.Date, nullable=True)

    # questions = db.relationship("QuestionsTable", back_populates="tests", lazy="dynamic", cascade="all, delete")


