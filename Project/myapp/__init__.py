from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))
flaskObj = Flask(__name__)

flaskObj.config.from_mapping(
        SECRET_KEY = 'mypassword',
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "appdb"),
        SQLALCHEMY_TRACK_MODIFICATIONS = False,

)

db = SQLAlchemy(flaskObj)

from myapp.routes import homepage