import unittest
from flask import url_for

from application import app

class TestViews():
	response = self.client.get(url_for('/'))
	self.assertEqual(response.staus_code, 200)
