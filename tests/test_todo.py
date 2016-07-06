import unittest
from app import app

class TodoTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        print('down')

    def test_index(self):
        rv = self.app.get('/')
        assert "Todo" in str(rv.data)
