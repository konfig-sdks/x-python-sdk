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

from x_python_sdk.pydantic.tweet_id import TweetId

class TweetReferencedTweetsItem(BaseModel):
    id: TweetId = Field(alias='id')

    type: Literal["retweeted", "quoted", "replied_to"] = Field(alias='type')
    class Config:
        arbitrary_types_allowed = True
