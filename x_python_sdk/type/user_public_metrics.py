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


class RequiredUserPublicMetrics(TypedDict):
    # Number of Users who are following this User.
    followers_count: int

    # Number of Users this User is following.
    following_count: int

    # The number of lists that include this User.
    listed_count: int

    # The number of Tweets (including Retweets) posted by this User.
    tweet_count: int

class OptionalUserPublicMetrics(TypedDict, total=False):
    pass

class UserPublicMetrics(RequiredUserPublicMetrics, OptionalUserPublicMetrics):
    pass
