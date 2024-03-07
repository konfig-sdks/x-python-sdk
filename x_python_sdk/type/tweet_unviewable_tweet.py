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
from x_python_sdk.type.user_id import UserId

class RequiredTweetUnviewableTweet(TypedDict):
    author_id: UserId

    id: TweetId

class OptionalTweetUnviewableTweet(TypedDict, total=False):
    pass

class TweetUnviewableTweet(RequiredTweetUnviewableTweet, OptionalTweetUnviewableTweet):
    pass
