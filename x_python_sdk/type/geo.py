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

from x_python_sdk.type.geo_bbox import GeoBbox
from x_python_sdk.type.point import Point

class RequiredGeo(TypedDict):
    bbox: GeoBbox

    properties: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    type: str

class OptionalGeo(TypedDict, total=False):
    geometry: Point

class Geo(RequiredGeo, OptionalGeo):
    pass
