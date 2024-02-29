from flask import Flask, jsonify
from flask_smorest import Api
from resources.user import blp as user_bp
from dotenv import load_dotenv

from database import db
import os


def create_app(db_url=None):
    app = Flask(__name__)
    load_dotenv()


    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
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


    return app