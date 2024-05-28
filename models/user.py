from database import db
from datetime import date

class UserTable(db.Model):
    __tablename__ = "user"

    username = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(256), nullable=False)
    gender = db.Column(db.Integer, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    sexual_interest = db.Column(db.Integer, nullable=False)

    # answers = db.relationship('AnswerTable', back_populates='user', cascade='all, delete')
    # matches1 = db.relationship('MatchTable', foreign_keys='MatchTable.user1_username', back_populates='user1',
    #                            cascade='all, delete')
    # matches2 = db.relationship('MatchTable', foreign_keys='MatchTable.user2_username', back_populates='user2',
    #                            cascade='all, delete')
    # slots = db.relationship('SlotTable', back_populates='user', cascade='all, delete')
    # problem_forms = db.relationship('ProblemFormTable', back_populates='user', cascade='all, delete')
    #
