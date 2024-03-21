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
from datetime import date
# Creating a Flask-Smorest Blueprint
blp = Blueprint("Users", "users", description="Operations on users")


@blp.route("/register")
class UserRegister(MethodView):

    @blp.arguments(UserRegisterSchema)
    def post(self, user_data):
        # Check if the given username already exists
        existing_user = UserTable.query.filter(
            or_(UserTable.username == user_data["username"])).first()

        if existing_user:
            abort(409, message="Given username or gender already exists")

        password = pbkdf2_sha256.hash(user_data["password"])

        user = UserTable(username=user_data["username"], gender=user_data["gender"], password=password,
                         date_of_birth=user_data["date_of_birth"], sexual_interest=user_data["sexual_interest"])

        # Add the user to the database
        db.session.add(user)
        db.session.commit()

        return {"message": "User created successfully"}, 201

@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        user = UserTable.query.filter(UserTable.username == user_data["username"]).first()


        # Verify the provided password against the hashed password
        if user and pbkdf2_sha256.verify(user_data["password"], user.password):

            return {"message": "Login successful"}, 201

        # Passwords do not match; abort with 401 status if credentials are invalid
        abort(401, message="Invalid credentials")

