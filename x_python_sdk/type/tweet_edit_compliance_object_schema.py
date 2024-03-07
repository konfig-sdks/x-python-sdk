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

from x_python_sdk.type.tweet_edit_compliance_object_schema_tweet import TweetEditComplianceObjectSchemaTweet
from x_python_sdk.type.tweet_id import TweetId

class RequiredTweetEditComplianceObjectSchema(TypedDict):
    edit_tweet_ids: typing.List[TweetId]

    # Event time.
    event_at: datetime

    initial_tweet_id: TweetId

    tweet: TweetEditComplianceObjectSchemaTweet

class OptionalTweetEditComplianceObjectSchema(TypedDict, total=False):
    pass

class TweetEditComplianceObjectSchema(RequiredTweetEditComplianceObjectSchema, OptionalTweetEditComplianceObjectSchema):
    pass
