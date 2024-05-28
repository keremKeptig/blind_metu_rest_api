from database import db


class ProblemTable(db.Model):
    __tablename__ = "problem_form"

    form_id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(256), unique=False, nullable=False)
    date = db.Column(db.Date, nullable=True)
    username = db.Column(db.String(80), db.ForeignKey("user.username"), unique=False, nullable=False)

    # user = db.relationship('UserTable', back_populates='problem_forms')
    #
