import unittest
from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from app import app


class TestBase(TestCase):

    def create_app(self):

        # pass in test configurations
        app.config.update(
            DEBUG=True
        )
        return app

    def setUp(self):
        """
        Will be called before every test
        """

    def tearDown(self):
        """
        Will be called after every test
        """

class TestApp(TestBase):
    def test_app(self):
        with self.client:
            response = self.client.get(
                url_for('home')
            )
            self.assert200(response)

if __name__ == '__main__':
    unittest.main()