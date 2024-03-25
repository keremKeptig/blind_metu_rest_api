from database import db


class ProblemTable(db.Model):
    __tablename__ = "problemForms"

    form_id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(256), unique=False, nullable=False)

    id = db.Column(db.String(80), db.ForeignKey("users.username"), unique=False, nullable=False)

    # user = db.relationship("UserTable", back_populates="problemForms")
