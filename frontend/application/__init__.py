
from flask import Flask
import os

from flask_sqlalchemy import SQLAlchemy

app = Flask (__name__)

db = SQLAlchemy(app)

from application import routes
