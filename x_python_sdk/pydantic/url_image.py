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

from x_python_sdk.pydantic.media_height import MediaHeight
from x_python_sdk.pydantic.media_width import MediaWidth

class UrlImage(BaseModel):
    height: typing.Optional[MediaHeight] = Field(None, alias='height')

    # A validly formatted URL.
    url: typing.Optional[str] = Field(None, alias='url')

    width: typing.Optional[MediaWidth] = Field(None, alias='width')
    class Config:
        arbitrary_types_allowed = True
