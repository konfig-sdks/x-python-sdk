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
from x_python_sdk.pydantic.user_id import UserId

class TweetCreateRequestReply(BaseModel):
    in_reply_to_tweet_id: TweetId = Field(alias='in_reply_to_tweet_id')

    # A list of User Ids to be excluded from the reply Tweet.
    exclude_reply_user_ids: typing.Optional[typing.List[UserId]] = Field(None, alias='exclude_reply_user_ids')
    class Config:
        arbitrary_types_allowed = True
