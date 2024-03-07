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


class Variant(BaseModel):
    # The bit rate of the media.
    bit_rate: typing.Optional[int] = Field(None, alias='bit_rate')

    # The content type of the media.
    content_type: typing.Optional[str] = Field(None, alias='content_type')

    # The url to the media.
    url: typing.Optional[str] = Field(None, alias='url')
    class Config:
        arbitrary_types_allowed = True
