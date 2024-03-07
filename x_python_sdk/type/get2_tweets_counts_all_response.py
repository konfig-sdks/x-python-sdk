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

from x_python_sdk.type.get2_tweets_counts_all_response_meta import Get2TweetsCountsAllResponseMeta
from x_python_sdk.type.problem import Problem
from x_python_sdk.type.search_count import SearchCount

class RequiredGet2TweetsCountsAllResponse(TypedDict):
    pass

class OptionalGet2TweetsCountsAllResponse(TypedDict, total=False):
    data: typing.List[SearchCount]

    errors: typing.List[Problem]

    meta: Get2TweetsCountsAllResponseMeta

class Get2TweetsCountsAllResponse(RequiredGet2TweetsCountsAllResponse, OptionalGet2TweetsCountsAllResponse):
    pass
