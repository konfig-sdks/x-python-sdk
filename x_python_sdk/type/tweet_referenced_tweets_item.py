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

from x_python_sdk.type.tweet_id import TweetId

class RequiredTweetReferencedTweetsItem(TypedDict):
    id: TweetId

    type: str

class OptionalTweetReferencedTweetsItem(TypedDict, total=False):
    pass

class TweetReferencedTweetsItem(RequiredTweetReferencedTweetsItem, OptionalTweetReferencedTweetsItem):
    pass
