import os
import requests
from flask import jsonify
from sqlalchemy import or_, func
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from database import db
from schemas import UserSchema, QuestionSchema
from models import TestTable, QuestionTable, AnswerTable
from datetime import datetime
import jinja2
from datetime import date
# Creating a Flask-Smorest Blueprint
blp = Blueprint("Questions", "questions", description="Operations on questions")


@blp.route("/question/<int:test_id>")
class Question(MethodView):

    @blp.response(200)
    def get(self, test_id):
        # Query questions based on test_id
        questions = QuestionTable.query.filter_by(test_id=test_id).all()
        if not questions:
            abort(404, message=f"No questions found for test_id {test_id}")

        question_texts = [(question.question_text, question.question_id) for question in questions]
        return jsonify(question_texts)


@blp.route("/question/<string:username>/<int:test_id>")
class UserCheckTestIsSolved(MethodView):

    @blp.response(200)
    def get(self, username, test_id):
        # Query questions based on test_id
        # not solved yet
        isTestSolved = 1

        questions = QuestionTable.query.filter_by(test_id=test_id).all()

        for question in questions:
            answers = AnswerTable.query.filter_by(q_id=question.q_id).all()
            for answer in answers:
                if answer.user_id == username:
                    isTestSolved = 0

        return isTestSolved

@blp.route("/question")
class TestFind(MethodView):

    @blp.response(200)
    def get(self):
        # tests = T estTable.query.all()
        tests = TestTable.query.all()

        date_format = "%Y/%m-%d"

        test_id = -1

        current_datetime = datetime.now()
        date_object = datetime.strptime(current_datetime.strftime("%Y-%m-%d"), "%Y-%m-%d")

        for test in tests:
            test_start_datetime = datetime.combine(test.start_date, datetime.min.time())
            test_end_datetime = datetime.combine(test.end_date, datetime.max.time())

            if test_start_datetime <= date_object <= test_end_datetime:
                test_id = test.test_id
                break

        return test_id

