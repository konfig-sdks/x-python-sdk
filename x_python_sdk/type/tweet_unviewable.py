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

from x_python_sdk.type.tweet_unviewable_tweet import TweetUnviewableTweet

class RequiredTweetUnviewable(TypedDict):
    # If the label is being applied or removed. Possible values are ‘apply’ or ‘remove’.
    application: str

    # Event time.
    event_at: datetime

    tweet: TweetUnviewableTweet

class OptionalTweetUnviewable(TypedDict, total=False):
    pass

class TweetUnviewable(RequiredTweetUnviewable, OptionalTweetUnviewable):
    pass
