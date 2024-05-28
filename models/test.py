from database import db


class TestTable(db.Model):
    __tablename__ = "test"

    test_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(80), unique=False, nullable=False)
    start_date = db.Column(db.Date, nullable=True)
    end_date = db.Column(db.Date, nullable=True)

    # questions = db.relationship("QuestionTable", back_populates="test", lazy="dynamic", cascade="all, delete")


