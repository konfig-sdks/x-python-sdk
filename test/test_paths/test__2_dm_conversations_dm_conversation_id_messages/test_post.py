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
from x_python_sdk.paths._2_dm_conversations_dm_conversation_id_messages import post
from x_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestModel2DmConversationsDmConversationIdMessages(ApiTestMixin, unittest.TestCase):
    """
    Model2DmConversationsDmConversationIdMessages unit test stubs
        Send a new message to a DM Conversation
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 201




if __name__ == '__main__':
    unittest.main()
