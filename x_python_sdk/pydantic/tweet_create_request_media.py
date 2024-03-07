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

from x_python_sdk.pydantic.media_id import MediaId
from x_python_sdk.pydantic.user_id import UserId

class TweetCreateRequestMedia(BaseModel):
    # A list of Media Ids to be attached to a created Tweet.
    media_ids: typing.List[MediaId] = Field(alias='media_ids')

    # A list of User Ids to be tagged in the media for created Tweet.
    tagged_user_ids: typing.Optional[typing.List[UserId]] = Field(None, alias='tagged_user_ids')
    class Config:
        arbitrary_types_allowed = True
