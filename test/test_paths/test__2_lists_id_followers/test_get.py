# coding: utf-8

"""
    Twitter API v2

    Twitter API v2 available endpoints

    The version of the OpenAPI document: 2.62
    Created by: https://developer.twitter.com/
"""

import unittest
from unittest.mock import patch

import urllib3

import x_python_sdk
from x_python_sdk.paths._2_lists_id_followers import get
from x_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestModel2ListsIdFollowers(ApiTestMixin, unittest.TestCase):
    """
    Model2ListsIdFollowers unit test stubs
        Returns User objects that follow a List by the provided List ID
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
