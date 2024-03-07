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

from x_python_sdk.pydantic.tweet_edit_compliance_object_schema_tweet import TweetEditComplianceObjectSchemaTweet
from x_python_sdk.pydantic.tweet_id import TweetId

class TweetEditComplianceObjectSchema(BaseModel):
    edit_tweet_ids: typing.List[TweetId] = Field(alias='edit_tweet_ids')

    # Event time.
    event_at: datetime = Field(alias='event_at')

    initial_tweet_id: TweetId = Field(alias='initial_tweet_id')

    tweet: TweetEditComplianceObjectSchemaTweet = Field(alias='tweet')
    class Config:
        arbitrary_types_allowed = True
