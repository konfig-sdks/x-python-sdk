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
from x_python_sdk.paths._2_users_id_likes_tweet_id import delete
from x_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestModel2UsersIdLikesTweetId(ApiTestMixin, unittest.TestCase):
    """
    Model2UsersIdLikesTweetId unit test stubs
        Causes the User (in the path) to unlike the specified Tweet
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
