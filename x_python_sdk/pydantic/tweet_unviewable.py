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

from x_python_sdk.pydantic.tweet_unviewable_tweet import TweetUnviewableTweet

class TweetUnviewable(BaseModel):
    # If the label is being applied or removed. Possible values are ‘apply’ or ‘remove’.
    application: str = Field(alias='application')

    # Event time.
    event_at: datetime = Field(alias='event_at')

    tweet: TweetUnviewableTweet = Field(alias='tweet')
    class Config:
        arbitrary_types_allowed = True
