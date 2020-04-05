import unittest
from application import app
from flask import url_for
from flask_testing import TestCase
from application import routes
import json

class TestViews(TestCase):
    def create_app(self):
        config_name = 'testing'
        return app

    def test_prize(self):
        randnum = routes.prize().json
        print(randnum)
        assert(randnum["Prize"] < 101)

    def test_prize2(self):
        randnum = routes.prize().json
        print(randnum)
        assert(randnum["Prize"] > 50)
