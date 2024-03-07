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

from x_python_sdk.pydantic.tweet_notice_tweet import TweetNoticeTweet

class TweetNotice(BaseModel):
    # If the label is being applied or removed. Possible values are ‘apply’ or ‘remove’.
    application: str = Field(alias='application')

    # Event time.
    event_at: datetime = Field(alias='event_at')

    # The type of label on the Tweet
    event_type: str = Field(alias='event_type')

    tweet: TweetNoticeTweet = Field(alias='tweet')

    # Information shown on the Tweet label
    details: typing.Optional[str] = Field(None, alias='details')

    # Link to more information about this kind of label
    extended_details_url: typing.Optional[str] = Field(None, alias='extended_details_url')

    # Title/header of the Tweet label
    label_title: typing.Optional[str] = Field(None, alias='label_title')
    class Config:
        arbitrary_types_allowed = True
