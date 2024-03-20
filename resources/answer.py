import os
import requests
from sqlalchemy import or_
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from sqlalchemy.exc import SQLAlchemyError

from database import db
from schemas import UserSchema, UserRegisterSchema, AnswerSchema
from models import UserTable, AnswerTable
import jinja2
from datetime import date
# Creating a Flask-Smorest Blueprint
blp = Blueprint("Answers", "answers", description="Operations on answers")


@blp.route("/answer/<string:username>/<int:q_id>")
class UserRegister(MethodView):

    @blp.arguments(AnswerSchema)
    @blp.response(201, AnswerSchema)
    def post(self, answer_data, username, q_id):
        user = UserTable.query.filter_by(username=username).first()

        answer = AnswerTable(**answer_data, user_id=user.id, q_id=q_id)
        try:
            db.session.add(answer)
            db.session.commit()
        except SQLAlchemyError as error:
            abort(
                500,
                message=str(error)
            )
        return answer
