from app import create_app
import unittest

# How to run this file ?
# Go to the flask-quickstart directory
# ie. the directory above this one
# and execuute the following from the terminal
# python -m unittest tests.test_main

# ../flask-quickstart$ python -m unittest tests.test_main

# You IDE / editor will most likely have a feature/extension
# that automatically discovers and runs tests.


class TestMain(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

    def test_main(self):
        rv = self.client.get('/')
        assert rv.status == '200 OK'

    def test_404(self):
        rv = self.client.get('/unknownendpoint')
        self.assertEqual(rv.status, '404 NOT FOUND')
