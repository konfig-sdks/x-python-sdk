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

from x_python_sdk.type.country_code import CountryCode
from x_python_sdk.type.tweet_id import TweetId
from x_python_sdk.type.tweet_takedown_compliance_schema_tweet import TweetTakedownComplianceSchemaTweet

class RequiredTweetTakedownComplianceSchema(TypedDict):
    # Event time.
    event_at: datetime

    tweet: TweetTakedownComplianceSchemaTweet

    withheld_in_countries: typing.List[CountryCode]

class OptionalTweetTakedownComplianceSchema(TypedDict, total=False):
    quote_tweet_id: TweetId

class TweetTakedownComplianceSchema(RequiredTweetTakedownComplianceSchema, OptionalTweetTakedownComplianceSchema):
    pass
