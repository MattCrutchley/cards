import unittest
from application import app
from flask import url_for
from flask_testing import TestCase

class TestViews(TestCase):
	response = self.client.get(url_for('/'))
	self.assertEqual(response.staus_code, 200)
