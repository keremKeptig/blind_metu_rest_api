import os
import requests
from flask import jsonify
from sqlalchemy import or_, func
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from database import db
from schemas import UserSchema, QuestionSchema
from models import QuestionTable,TestTable
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

        question_texts = [question.q_text for question in questions]
        return jsonify(question_texts)

@blp.route("/question")
class TestFind(MethodView):

    @blp.response(200)
    def get(self):
        # tests = TestTable.query.all()

        max_test_id = db.session.query(func.max(TestTable.test_id)).scalar()
        print("En yüksek test ID:", max_test_id)

        return max_test_id