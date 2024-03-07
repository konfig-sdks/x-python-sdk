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

from x_python_sdk.pydantic.media_key import MediaKey
from x_python_sdk.pydantic.poll_id import PollId

class TweetAttachments(BaseModel):
    # A list of Media Keys for each one of the media attachments (if media are attached).
    media_keys: typing.Optional[typing.List[MediaKey]] = Field(None, alias='media_keys')

    # A list of poll IDs (if polls are attached).
    poll_ids: typing.Optional[typing.List[PollId]] = Field(None, alias='poll_ids')
    class Config:
        arbitrary_types_allowed = True
