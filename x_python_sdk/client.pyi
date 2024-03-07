# coding: utf-8
"""
    Twitter API v2

    Twitter API v2 available endpoints

    The version of the OpenAPI document: 2.62
    Created by: https://developer.twitter.com/
"""

import typing
import inspect
from datetime import date, datetime
from x_python_sdk.client_custom import ClientCustom
from x_python_sdk.configuration import Configuration
from x_python_sdk.api_client import ApiClient
from x_python_sdk.type_util import copy_signature
from x_python_sdk.apis.tags.bookmarks_api import BookmarksApi
from x_python_sdk.apis.tags.compliance_api import ComplianceApi
from x_python_sdk.apis.tags.direct_messages_api import DirectMessagesApi
from x_python_sdk.apis.tags.general_api import GeneralApi
from x_python_sdk.apis.tags.lists_api import ListsApi
from x_python_sdk.apis.tags.spaces_api import SpacesApi
from x_python_sdk.apis.tags.tweets_api import TweetsApi
from x_python_sdk.apis.tags.users_api import UsersApi



class X(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.bookmarks: BookmarksApi = BookmarksApi(api_client)
        self.compliance: ComplianceApi = ComplianceApi(api_client)
        self.direct_messages: DirectMessagesApi = DirectMessagesApi(api_client)
        self.general: GeneralApi = GeneralApi(api_client)
        self.lists: ListsApi = ListsApi(api_client)
        self.spaces: SpacesApi = SpacesApi(api_client)
        self.tweets: TweetsApi = TweetsApi(api_client)
        self.users: UsersApi = UsersApi(api_client)
