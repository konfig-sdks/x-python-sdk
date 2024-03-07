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


class RequiredTweetNonPublicMetrics(TypedDict):
    pass

class OptionalTweetNonPublicMetrics(TypedDict, total=False):
    # Number of times this Tweet has been viewed.
    impression_count: int

class TweetNonPublicMetrics(RequiredTweetNonPublicMetrics, OptionalTweetNonPublicMetrics):
    pass
