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


class TweetOrganicMetrics(BaseModel):
    # Number of times this Tweet has been viewed.
    impression_count: int = Field(alias='impression_count')

    # Number of times this Tweet has been liked.
    like_count: int = Field(alias='like_count')

    # Number of times this Tweet has been replied to.
    reply_count: int = Field(alias='reply_count')

    # Number of times this Tweet has been Retweeted.
    retweet_count: int = Field(alias='retweet_count')
    class Config:
        arbitrary_types_allowed = True
