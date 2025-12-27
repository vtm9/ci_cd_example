import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import json

import app as tested_app


class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        tested_app.app.config["TESTING"] = True
        self.app = tested_app.app.test_client()

    def test_multiply_success(self):
        r = self.app.get("/multiply?a=2&b=3")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, b"6.0")

    def test_divide_success(self):
        r = self.app.get("/divide?a=6&b=2")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, b"3.0")

    def test_divide_by_zero(self):
        r = self.app.get("/divide?a=6&b=0")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data.decode("utf-8"), "Деление на ноль невозможно")


if __name__ == "__main__":
    unittest.main()
