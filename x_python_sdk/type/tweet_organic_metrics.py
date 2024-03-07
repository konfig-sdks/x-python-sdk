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


class RequiredTweetOrganicMetrics(TypedDict):
    # Number of times this Tweet has been viewed.
    impression_count: int

    # Number of times this Tweet has been liked.
    like_count: int

    # Number of times this Tweet has been replied to.
    reply_count: int

    # Number of times this Tweet has been Retweeted.
    retweet_count: int

class OptionalTweetOrganicMetrics(TypedDict, total=False):
    pass

class TweetOrganicMetrics(RequiredTweetOrganicMetrics, OptionalTweetOrganicMetrics):
    pass
