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
from pydantic import BaseModel, Field, RootModel

from x_python_sdk.pydantic.country_code import CountryCode
from x_python_sdk.pydantic.tweet_id import TweetId
from x_python_sdk.pydantic.tweet_takedown_compliance_schema_tweet import TweetTakedownComplianceSchemaTweet

class TweetTakedownComplianceSchema(BaseModel):
    # Event time.
    event_at: datetime = Field(alias='event_at')

    tweet: TweetTakedownComplianceSchemaTweet = Field(alias='tweet')

    withheld_in_countries: typing.List[CountryCode] = Field(alias='withheld_in_countries')

    quote_tweet_id: typing.Optional[TweetId] = Field(None, alias='quote_tweet_id')
    class Config:
        arbitrary_types_allowed = True
