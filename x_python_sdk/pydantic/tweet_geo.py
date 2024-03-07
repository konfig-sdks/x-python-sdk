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

from x_python_sdk.pydantic.point import Point

class TweetGeo(BaseModel):
    coordinates: typing.Optional[Point] = Field(None, alias='coordinates')

    # The identifier for this place.
    place_id: typing.Optional[str] = Field(None, alias='place_id')
    class Config:
        arbitrary_types_allowed = True
