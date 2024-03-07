# coding: utf-8

"""
    Twitter API v2

    Twitter API v2 available endpoints

    The version of the OpenAPI document: 2.62
    Created by: https://developer.twitter.com/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from x_python_sdk.type.expansions import Expansions
from x_python_sdk.type.get2_tweets_search_all_response_meta import Get2TweetsSearchAllResponseMeta
from x_python_sdk.type.problem import Problem
from x_python_sdk.type.tweet import Tweet

class RequiredGet2TweetsSearchAllResponse(TypedDict):
    pass

class OptionalGet2TweetsSearchAllResponse(TypedDict, total=False):
    data: typing.List[Tweet]

    errors: typing.List[Problem]

    includes: Expansions

    meta: Get2TweetsSearchAllResponseMeta

class Get2TweetsSearchAllResponse(RequiredGet2TweetsSearchAllResponse, OptionalGet2TweetsSearchAllResponse):
    pass
