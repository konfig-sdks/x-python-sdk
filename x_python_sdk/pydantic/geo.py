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

from x_python_sdk.pydantic.geo_bbox import GeoBbox
from x_python_sdk.pydantic.point import Point

class Geo(BaseModel):
    bbox: GeoBbox = Field(alias='bbox')

    properties: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='properties')

    type: Literal["Feature"] = Field(alias='type')

    geometry: typing.Optional[Point] = Field(None, alias='geometry')
    class Config:
        arbitrary_types_allowed = True
