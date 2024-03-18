from database import db
from datetime import date

class UserTable(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    gender = db.Column(db.Integer, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    sexual_interest = db.Column(db.Integer, nullable=False)

    schedule_id = db.Column(db.Integer, db.ForeignKey("schedules.schedule_id"), unique=False, nullable=True)


    answers = db.relationship('AnswerTable', back_populates='users', cascade='all, delete')
    questions = db.relationship('QuestionTable', back_populates='users', cascade='all, delete')
    matches = db.relationship('MatchTable', back_populates='users', cascade='all, delete')

