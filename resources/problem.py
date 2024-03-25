import os
import requests
from sqlalchemy import or_
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from sqlalchemy.exc import SQLAlchemyError

from database import db
from schemas import ProblemSchema
from models import UserTable, ProblemTable
import jinja2
from datetime import date
# Creating a Flask-Smorest Blueprint
blp = Blueprint("ProblemForms", "problemForms", description="Operations on forms")


@blp.route("/problemform/<string:username>")
class ProblemForm(MethodView):

    @blp.arguments(ProblemSchema)
    @blp.response(201, ProblemSchema)
    def post(self, problem_data, username):
        user = UserTable.query.get_or_404(username)

        problem_comment = ProblemTable(**problem_data,id=user.username)
        try:
            db.session.add(problem_comment)
            db.session.commit()
        except SQLAlchemyError as error:
            abort(
                500,
                message=str(error)
            )
        return problem_comment