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

from x_python_sdk.type.tweet_notice_tweet import TweetNoticeTweet

class RequiredTweetNotice(TypedDict):
    # If the label is being applied or removed. Possible values are ‘apply’ or ‘remove’.
    application: str

    # Event time.
    event_at: datetime

    # The type of label on the Tweet
    event_type: str

    tweet: TweetNoticeTweet

class OptionalTweetNotice(TypedDict, total=False):
    # Information shown on the Tweet label
    details: str

    # Link to more information about this kind of label
    extended_details_url: str

    # Title/header of the Tweet label
    label_title: str

class TweetNotice(RequiredTweetNotice, OptionalTweetNotice):
    pass
