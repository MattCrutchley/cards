import unittest
from application import app
from flask import url_for
from flask_testing import TestCase

class TestViews(TestCase):
    def create_app(self):
        config_name = 'testing'
        return app

    def test_views_home(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.staus_code, 200)
