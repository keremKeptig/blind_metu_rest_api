from flask import Flask, jsonify
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy

from resources.user import blp as user_bp
from resources.questions import blp as question_blp
from resources.answer import blp as answ_blp
from resources.problem import blp as problem_blp
from resources.matchAlgorithm import blp as match_blp
from dotenv import load_dotenv
from flask_migrate import Migrate

from database import db
import os


def create_app(db_url=None):
    app = Flask(__name__)
    load_dotenv()


    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "REST API blind"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    api = Api(app)

    app.config["JWT_SECRET_KEY"] = "80667524238808854628174589614279646612"


    with app.app_context():
        db.create_all()
    api.register_blueprint(user_bp)
    api.register_blueprint(question_blp)
    api.register_blueprint(answ_blp)
    api.register_blueprint(problem_blp)
    api.register_blueprint(match_blp)

    return app