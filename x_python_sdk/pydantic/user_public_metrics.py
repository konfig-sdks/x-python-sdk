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


class UserPublicMetrics(BaseModel):
    # Number of Users who are following this User.
    followers_count: int = Field(alias='followers_count')

    # Number of Users this User is following.
    following_count: int = Field(alias='following_count')

    # The number of lists that include this User.
    listed_count: int = Field(alias='listed_count')

    # The number of Tweets (including Retweets) posted by this User.
    tweet_count: int = Field(alias='tweet_count')
    class Config:
        arbitrary_types_allowed = True
