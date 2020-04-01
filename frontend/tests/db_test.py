import unittest
import os

from flask import abort, url_for
from flask_testing import TestCase

from application import app, db
"""
class TestBase(TestCase):

    def create_app(self):
        config_name = 'testing'
        app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('TEST_DATABASE_URI'))
        app.config['SECRET_KEY'] = str(os.getenv('SECRET_KEY'))
        return appa
"""
