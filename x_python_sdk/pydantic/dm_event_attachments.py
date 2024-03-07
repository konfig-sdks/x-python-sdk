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

from x_python_sdk.pydantic.dm_event_attachments_card_ids import DmEventAttachmentsCardIds
from x_python_sdk.pydantic.media_key import MediaKey

class DmEventAttachments(BaseModel):
    card_ids: typing.Optional[DmEventAttachmentsCardIds] = Field(None, alias='card_ids')

    # A list of Media Keys for each one of the media attachments (if media are attached).
    media_keys: typing.Optional[typing.List[MediaKey]] = Field(None, alias='media_keys')
    class Config:
        arbitrary_types_allowed = True
