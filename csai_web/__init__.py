import flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)#, static_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Authentication.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '550b60f22753958ce551a7d753e17889'

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["100 per hour", "20 per minute"]
)

db = SQLAlchemy(app)