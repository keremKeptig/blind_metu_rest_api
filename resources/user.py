import os
import requests
from sqlalchemy import or_
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from database import db
from schemas import UserSchema, UserRegisterSchema
from models import UserTable
import jinja2

# Creating a Flask-Smorest Blueprint
blp = Blueprint("Users", "users", description="Operations on users")


@blp.route("/register")
class UserRegister(MethodView):

    @blp.arguments(UserRegisterSchema)
    def post(self, user_data):
        # Check if the given username or gedner already exists
        existing_user = UserTable.query.filter(
            or_(UserTable.username == user_data["username"], UserTable.gender == user_data["gender"])).first()

        if existing_user:
            abort(409, message="Given username or gender already exists")

        password = pbkdf2_sha256.hash(user_data["password"])


        # Create a new user without storing the password in my database
        user = UserTable(username=user_data["username"], gender=user_data["gender"], password=password)

        # Add the user to the database
        db.session.add(user)
        db.session.commit()

        return {"message": "User created successfully"}, 201
