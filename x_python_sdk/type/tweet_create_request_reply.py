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

class RequiredTweetCreateRequestReply(TypedDict):
    in_reply_to_tweet_id: TweetId

class OptionalTweetCreateRequestReply(TypedDict, total=False):
    # A list of User Ids to be excluded from the reply Tweet.
    exclude_reply_user_ids: typing.List[UserId]

class TweetCreateRequestReply(RequiredTweetCreateRequestReply, OptionalTweetCreateRequestReply):
    pass
