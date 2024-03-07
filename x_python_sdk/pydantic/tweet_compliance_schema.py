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

from x_python_sdk.pydantic.tweet_compliance_schema_tweet import TweetComplianceSchemaTweet
from x_python_sdk.pydantic.tweet_id import TweetId

class TweetComplianceSchema(BaseModel):
    # Event time.
    event_at: datetime = Field(alias='event_at')

    tweet: TweetComplianceSchemaTweet = Field(alias='tweet')

    quote_tweet_id: typing.Optional[TweetId] = Field(None, alias='quote_tweet_id')
    class Config:
        arbitrary_types_allowed = True
