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

from x_python_sdk.type.tweet_create_request_poll_options import TweetCreateRequestPollOptions

class RequiredTweetCreateRequestPoll(TypedDict):
    # Duration of the poll in minutes.
    duration_minutes: int

    options: TweetCreateRequestPollOptions

class OptionalTweetCreateRequestPoll(TypedDict, total=False):
    # Settings to indicate who can reply to the Tweet.
    reply_settings: str

class TweetCreateRequestPoll(RequiredTweetCreateRequestPoll, OptionalTweetCreateRequestPoll):
    pass
