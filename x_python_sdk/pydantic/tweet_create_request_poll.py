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

from x_python_sdk.pydantic.tweet_create_request_poll_options import TweetCreateRequestPollOptions

class TweetCreateRequestPoll(BaseModel):
    # Duration of the poll in minutes.
    duration_minutes: int = Field(alias='duration_minutes')

    options: TweetCreateRequestPollOptions = Field(alias='options')

    # Settings to indicate who can reply to the Tweet.
    reply_settings: typing.Optional[Literal["following", "mentionedUsers"]] = Field(None, alias='reply_settings')
    class Config:
        arbitrary_types_allowed = True
