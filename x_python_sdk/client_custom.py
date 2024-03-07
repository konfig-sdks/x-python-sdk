# coding: utf-8
"""
    Twitter API v2

    Twitter API v2 available endpoints

    The version of the OpenAPI document: 2.62
    Created by: https://developer.twitter.com/
"""

import typing

from x_python_sdk.configuration import Configuration
from x_python_sdk.api_client import ApiClient



class ClientCustom:

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        # customize here

    # add custom methods here