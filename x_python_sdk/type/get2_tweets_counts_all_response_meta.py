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

from x_python_sdk.type.next_token import NextToken

class RequiredGet2TweetsCountsAllResponseMeta(TypedDict):
    pass

class OptionalGet2TweetsCountsAllResponseMeta(TypedDict, total=False):
    # The newest id in this response.
    newest_id: str

    next_token: NextToken

    # The oldest id in this response.
    oldest_id: str

    # The sum of results returned in this response.
    total_tweet_count: int

class Get2TweetsCountsAllResponseMeta(RequiredGet2TweetsCountsAllResponseMeta, OptionalGet2TweetsCountsAllResponseMeta):
    pass
