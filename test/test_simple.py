# coding: utf-8

"""
    Twitter API v2

    Twitter API v2 available endpoints

    The version of the OpenAPI document: 2.62
    Created by: https://developer.twitter.com/
"""

import unittest

import os
from pprint import pprint
from x_python_sdk import X

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        x = X(
        
            access_token = 'YOUR_BEARER_TOKEN',
        
            client_id = 'YOUR_CLIENT_ID',
            client_secret = 'YOUR_CLIENT_SECRET',,
        )
        self.assertIsNotNone(x)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
